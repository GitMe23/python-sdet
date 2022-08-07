import requests
import json
from utilities.configurations import *

config = getConfig()

response = requests.get(config['API']['endpoint']+'/Library/GetBook.php',
             params={'AuthorName':'Rahul Shetty'},)
print(response.text)
print(type(response.text))
dict_response = json.loads(response.text)
print(dict_response[0]['isbn'])
json_response = response.json()
print(type(json_response))
print(json_response[0]['isbn'])
assert response.status_code == 200
print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
# Retrieve the book details with ISBN RGHCC
for actualBook in json_response:
    if actualBook['isbn'] == 'RGHCC':
        print(actualBook)
        break
















