from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# create an instance of my flask class so as to generate a new flask app
app = Flask(__name__)

#configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:allcowseatgrass@127.0.0.1:5432/book_manager'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# create an instance of the SQLAlchemy class
db = SQLAlchemy(app)

# create an instance of the Migrate class
migrate = Migrate(app, db)

#import my models 
from models.book import Book
from models.member import Member
from models.user import User

@app.route('/')
def home():

    message = {"message": "Welcome to my book manager API!"}

    return jsonify(message)

@app.route('/books', methods=['GET', 'POST', 'PUT', 'DELETE'])
def books():

    if request.method == 'GET':
        all_books = db.session.query(Book).all()
        return jsonify(all_books)
    
    elif request.method == 'POST':

        # get the data from the request
        data = request.get_json()

        # create a new book object
        new_book = Book(author=data['author'], isbn=data['isbn'], is_lent=data['is_lent'])

        # add the book to the database
        db.session.add(new_book)

        # commit the changes
        db.session.commit()

        return jsonify({"book": new_book, "message": "You have added a new book!"})
        
    elif request.method == 'PUT':
        return "You have updated a book"
    elif request.method == 'DELETE':
        return "You have deleted a book"
    return "Here are all the books!"

# @app.route('/books/<int:book_id>/<string:book_name>')
# def book(book_id, book_name):
#     return f"Here is the book with id {book_id} {book_name}!"

if __name__ == '__main__':
    app.run(debug=True)