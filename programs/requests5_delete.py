

import requests

url = "https://dummyjson.com/"
endpoint = "products/1"
finalurl = url + endpoint
response = requests.delete(finalurl)

print("Status code:", response.status_code)
print(response.json())