import requests
import json
import os

WEBHOOK_URL = os.environ.get('WEBHOOK_URL')
AVATAR_URL = os.environ.get('AVATAR_URL')


def push_message(message: str):
    webhook_url = WEBHOOK_URL
    main_content = {
        "username": "Amazon Web Services",
        "avatar_url": AVATAR_URL,
        "content": message,
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook_url, json.dumps(main_content), headers=headers)
    print(response)
