from flask import Flask, request, jsonify

app = Flask(__name__) # Create server, 

# Create a data store

books_published = []   # A real app would store this persistently, empty list to start with

# @app.route() is a decorator that tells Flask what URL should trigger our function
@app.route('/books')
def all_books(): # function to get all books, this is the function that will be called when we access the /books URL
    return jsonify(books_published)

# This is the function that will be called when we access the /book URL with a POST request, this is how we will add a new book to our data store
@app.route('/book', methods=['POST'])
def add_book():
    new_book = request.form # get the data from request, this is how we will get the data that the client sends to us when they want to add a new book
    name = new_book.get('name')
    if not name:
        return 'No book name provided', 400
    if name not in books_published:
        books_published.append(name)
        return 'Added', 201
    else:
        return 'Duplicate book', 400


# Run the app, this will start the server and make it listen for requests, this is the end of the code
if __name__ == '__main__':
    app.run() # Removed debug mode 

