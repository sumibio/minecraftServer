import json
import os
from datetime import datetime
from handler.notification_for_discord import push_message


import boto3


DOMAIN_NAME = os.environ.get('DOMAIN_NAME')
HOSTEDZONE_ID = os.environ.get('HOSTEDZONE_ID')


def json_dt(o):
    if isinstance(o, datetime):
        return o.isoformat()


def change_record(action, host_name, host_addr):
    domain_name = DOMAIN_NAME
    if domain_name:
        host_name = F"{host_name}.{domain_name}."
    client = boto3.client('route53')
    change_batch = {
        "Comment": "optional comment about the changes in this change batch request",
        "Changes": [
            {
                "Action": action,
                "ResourceRecordSet": {
                    "Name": host_name,
                    "Type": "A",
                    "TTL": 300,
                    "ResourceRecords": [
                        {
                            "Value": host_addr
                        }
                    ]
                }
            }
        ]
    }
    print("change_batch: " + json.dumps(change_batch, default=json_dt))
    response = client.change_resource_record_sets(
        HostedZoneId=HOSTEDZONE_ID,
        ChangeBatch=change_batch
    )
    print("result: " + json.dumps(response, default=json_dt))
    return response


def get_hostname_from_tags(tags):
    host_name = ''
    for tag in tags:
        if tag['Key'].lower() == 'hostname':
            host_name = tag['Value'].lower()
    return host_name


def check_action(state):
    if state == 'running':
        action = 'UPSERT'
        push_message('インスタンスを起動しました。:dog:')
    elif state == 'stopping':
        action = 'DELETE'
        push_message('インスタンスを停止しました。:cat:')
    else:
        action = ''
    return action


def lambda_handler(event, context):
    result = dict()
    print('event: ' + json.dumps(event, default=json_dt))
    action = check_action(event['detail']['state'])
    if action:
        ec2 = boto3.resource('ec2')
        instance = ec2.Instance(event['detail']['instance-id'])
        host_name = get_hostname_from_tags(instance.tags)
        if host_name:
            host_addr = instance.public_ip_address
            result = change_record(action, host_name, host_addr)
    return json.dumps(result, default=json_dt)
