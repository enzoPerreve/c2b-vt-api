import requests
import json

# Read the json data
with open('json.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

# Post to the endpoint
url = 'http://localhost:8000/get-asset-id'
response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())