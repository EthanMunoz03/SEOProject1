import requests

url = 'https://httpbin.org/post'
response = requests.post(url)

data = response.json()

print(data)