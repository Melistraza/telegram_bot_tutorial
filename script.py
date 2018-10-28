#!/usr/bin/env python3

import requests

TOKEN = 'your_token'

API_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

reply_payload = {
    'chat_id': 190564045,
    'text': 'Hola <username>'
}

request = requests.post(API_URL, data=reply_payload)

print(request.json())
