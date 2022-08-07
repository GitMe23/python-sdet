import requests

#  hitting request with payload and adding headers
addBook_response = requests.post('http://216.10.245.166/Library/Addbook.php',
                                 json={
                                     "name": "Moby Dick",
                                     "isbn": "z123s",
                                     "aisle": "2289",
                                     "author": "Herman Melville"
                                 }, headers={"Content-Type": "application/json"},
                                 )

print(addBook_response.json())

json_response = addBook_response.json()

bookId = json_response['ID']
print(bookId)

delete_response = requests.post('http://216.10.245.166/Library/DeleteBook.php',
                                json={
                                    "ID": bookId
                                }, headers={"Content-Type": "application/json"},
                                )

assert delete_response.status_code == 200
delete_json_response = delete_response.json()
print(delete_json_response['msg'])
