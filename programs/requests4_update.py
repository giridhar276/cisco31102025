import requests
url = "https://dummyjson.com/"
endpoint = "products/1"
finalurl = url + endpoint
payload = {
    "title": "Simple Demo Product test",
    "price": 10000
}
# requests.put is equal to update query
response = requests.put(finalurl, json=payload)

print("Status code:", response.status_code)
print(response.json())
