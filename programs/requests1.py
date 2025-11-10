import requests
import json
url = "https://dummyjson.com/"
endpoint = "products"
finalurl = url + endpoint
response = requests.get(finalurl)
print("Status code:", response.status_code)
if response.status_code == 200:
    #print(response.json())
    data = response.json()
    for item in data['products']:
        print(item['title'])

