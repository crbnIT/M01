from flask import Flask
from flask import jsonify
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy


app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///books.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.book_name}, {self.author}, {self.publisher}"

@app.route("/")
def index():
    return "Hello"

@app.route("/books")
def get_books():
    books = db.session.query(Book).all()
    return jsonify([{"book_name": book.book_name, "author": book.author, "publisher": book.publisher} for book in books])

def init_db():
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    app.run(debug=True)