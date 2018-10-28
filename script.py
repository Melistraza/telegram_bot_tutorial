#!/usr/bin/env python3

import requests

TOKEN = 'your_token'

API_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

request = requests.get(API_URL)

print(request.json())
