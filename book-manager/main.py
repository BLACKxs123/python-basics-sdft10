from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# create an instance of my flask class so as to generate a new flask app
app = Flask(__name__)

#configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# create an instance of the SQLAlchemy class
db = SQLAlchemy(app)

# create an instance of the Migrate class
migrate = Migrate(app, db)

#import my models 
from models.book import Book
from models.member import Member
from models.user import User

books_list = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
]

@app.route('/')
def home():

    message = {"message": "Welcome to my book manager API!"}

    return jsonify(message)

@app.route('/books', methods=['GET', 'POST', 'PUT', 'DELETE'])
def books():

    if request.method == 'GET':
        return jsonify(books_list)
    elif request.method == 'POST':
        new_book = {"id": 4, "title": "The Catcher in the Rye", "author": "J.D"}
        books_list.append(new_book)
        return jsonify(books_list)
    elif request.method == 'PUT':
        updated_book = {"id": 1, "title": "Seth Gor", "author": "George Orwell"}
        books_list[0] = updated_book
        return jsonify(books_list)
    elif request.method == 'DELETE':
        books_list.pop(0)
        return jsonify(books_list)
    return "Here are all the books!"

@app.route('/books/<int:book_id>/<string:book_name>')
def book(book_id, book_name):
    return f"Here is the book with id {book_id} {book_name}!"

if __name__ == '__main__':
    app.run(debug=True)