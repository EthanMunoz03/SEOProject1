import requests

url = "https://jsonplaceholder.typicode.com/posts"

title = "Special Agent"

response = requests.post(url, data = {'title': 'Special Agent', 'body': 'Leroy Jethro Gibbs', 'userId': '1'})

print(response.status_code)

print(response.json())