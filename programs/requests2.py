

import requests

url = "https://dummyjson.com/products/1"

response = requests.get(url)

print("Status code:", response.status_code)
print(response.json())