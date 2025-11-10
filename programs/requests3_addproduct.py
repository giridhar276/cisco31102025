import requests
url = "https://dummyjson.com/"
endpoint = "products/add"
finalurl = url + endpoint
payload = {
    "title": "Simple Demo Product",
    "price": 1000
}
## requests.post is same as insert query
response = requests.post(finalurl, json=payload)
print("Status code:", response.status_code)
if response.status_code == 200:
    print(response.json())
