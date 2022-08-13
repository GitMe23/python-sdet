import requests

from utilities import pass_manager
from utilities.configurations import *
from payLoad import *
from utilities.resources import *
from utilities.pass_manager import *

config = getConfig()

add_url = getConfig()['API']['endpoint'] + ApiResources.add_book
headers = {"Content-Type": "application/json"}

#  hitting request with payload and adding headers
addBook_response = requests.post(add_url,
                                 json=addBookPayload("randomISBN"),
                                 headers=headers,
                                 )

print(addBook_response.json())

json_response = addBook_response.json()

bookId = json_response['ID']
print(bookId)

del_url = getConfig()['API']['endpoint'] + ApiResources.delete_book
delete_response = requests.post(del_url,
                                json={
                                    "ID": bookId
                                }, headers=headers,
                                )

assert delete_response.status_code == 200
delete_json_response = delete_response.json()
print(delete_json_response['msg'])

# Authentication
url = "http://api.github.com/user"
github_response = requests.get(url, verify=False, auth=())
print(github_response.status_code)
