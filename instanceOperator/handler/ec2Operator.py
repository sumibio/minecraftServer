import os
import json
import boto3

REGION = 'ap-northeast-1'
INSTANCE_ID = os.environ.get('INSTANSID')


def status_checker(describe_instances: dict) -> str:
    if describe_instances['ResponseMetadata']['HTTPStatusCode'] == 200:
        state = describe_instances['Reservations'][0]['Instances'][0]['State']['Name']
    else:
        state = 'http response error'
        print(state)
    return state


def start(instans_id: str) -> int:
    try:
        ec2_client = boto3.client('ec2', region_name=REGION)
        describe_instances = ec2_client.describe_instances(InstanceIds=[instans_id])
        print(describe_instances)
        if status_checker(describe_instances) == 'stopped':
            ec2_client.start_instances(InstanceIds=[instans_id])
            print('instans start')
        else:
            print('instans not stopped')
            return 1
    except Exception as e:
        print(e)
        return 2
    return 0


def stop(instans_id: str) -> int:
    try:
        ec2_client = boto3.client('ec2', region_name=REGION)
        describe_instances = ec2_client.describe_instances(InstanceIds=[instans_id])
        if status_checker(describe_instances) == 'running':
            ec2_client.stop_instances(InstanceIds=[instans_id])
            print('instans start')
        else:
            print('instans not running')
            return 1
    except Exception as e:
        print(e)
        return 2
    return 0


def lambda_handler(event, context):
    status = 200
    message = ''
    if event['headers']['action'] == 'startup':
        res = start(INSTANCE_ID)
        if res == 0:
            status = 200
            message = 'インスタンスを起動処理を開始しました。'
        elif res == 1:
            status = 201
            message = 'インスタンスが停止していません。'
        elif res == 2:
            status = 202
            message = '例外が発生しました。詳細はLambda関数のログを確認してください。'

    elif event['headers']['action'] == 'stop':
        res = stop(INSTANCE_ID)
        if res == 0:
            status = 200
            message = 'インスタンスを停止処理を開始しました。'
        elif res == 1:
            status = 201
            message = 'インスタンスが起動していません。'
        elif res == 2:
            status = 202
            message = '例外が発生しました。詳細はLambda関数のログを確認してください。'
    else:
        message = '定義されていないactionです。'

    return {
        'statusCode': status,
        'body': json.dumps({"message": message})
    }
