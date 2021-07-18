import os
import json
import boto3
import handler.operation_parameter as operation_parameter


REGION = 'ap-northeast-1'
INSTANCE_ID = os.environ.get('INSTANCEID')


def status_checker(describe_instances: dict) -> str:
    if describe_instances['ResponseMetadata']['HTTPStatusCode'] == 200:
        state = describe_instances['Reservations'][0]['Instances'][0]['State']['Name']
    else:
        print('http response error')
    print('state: ' + state)
    return state


def operation(instasce_id: str, expectation: str, method_name: str) -> int:
    try:
        ec2_client = boto3.client('ec2', region_name=REGION)
        describe_instances = ec2_client.describe_instances(InstanceIds=[instasce_id])
        if status_checker(describe_instances) == expectation:
            method = getattr(ec2_client, method_name)
            method(InstanceIds=[instasce_id])
        else:
            return 201
    except Exception as e:
        print(e)
        return 202
    return 200


def lambda_handler(event, context):
    action = event['headers']['action']
    if operation_parameter.key_check(action) == 0:
        method_name = operation_parameter.get_parameter(action, 'method_name')
        expectation = operation_parameter.get_parameter(action, 'expectation')
        status = operation(INSTANCE_ID, expectation, method_name)
        message = operation_parameter.get_parameter(action, 'message')[status]
    else:
        status = 203
        message = '定義されていないactionです。'

    return {
        'statusCode': status,
        'body': json.dumps({"message": message})
    }
