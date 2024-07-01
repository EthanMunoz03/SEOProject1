import requests

url = 'http://text-processing.com/api/sentiment/'

somevalue = input('enter text: ')

myobj = {'text': somevalue}
response = requests.post(url, data = myobj)

data = response.json()

print(data)