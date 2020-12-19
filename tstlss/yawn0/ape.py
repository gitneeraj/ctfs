#!/usr/bin/env python3

import requests

url = "https://okboomer.tasteless.eu:10401/rolling"
# path = "/rolling"

response = requests.get(url)
print(response.text)