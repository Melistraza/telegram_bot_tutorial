#!/usr/bin/env python3

import requests

TOKEN = 'your_token'

API_URL = f'https://api.telegram.org/bot{TOKEN}/getMe'

request = requests.get(API_URL)

print(request.json())
