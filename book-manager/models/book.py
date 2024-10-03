from main import db

class Book(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    author = db.Column(db.String(256), nullable=False)
    isbn = db.Column(db.String(256), nullable=False)
    is_lent = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"Book {self.id}"