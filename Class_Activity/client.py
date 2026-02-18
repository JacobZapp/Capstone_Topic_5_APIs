import requests

# Make a GET request to the /books endpoint to get the list of books, this is just to show that we can make a request to the server, we will add more requests later
response = requests.get('http://127.0.0.1:5000/books')

new_book = {'name': 'Lord of the Flies'}
add_book_response = requests.post('http://127.0.0.1:5000/book', data=new_book)
print(add_book_response.status_code)

all_books_response = requests.get('http://127.0.0.1:5000/books')
print(all_books_response.json())
