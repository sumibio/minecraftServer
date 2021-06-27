import requests
import json
import os

WEBHOOKURL = os.environ.get('WEBHOOKURL')


def push_message(message: str):
    webhook_url = WEBHOOKURL
    main_content = {
        "username": "Amazon Web Services",
        "avatar_url": "https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png",
        "content": message,
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook_url, json.dumps(main_content), headers=headers)
    print(response)
