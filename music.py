from urllib import request
import sqlite3
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import Integer,String, Float

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///bookscollections.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    title: Mapped[str] = mapped_column(String(250),unique=True,nullable=False)
    author = Mapped[float] = mapped_column(Float,nullable=False)

    with app.app_context():
        db.create_all()

    def addToBook(self):
        new_book = Book(id=1,title="Harry Porter",Author="J.K Rowling", rating=9.3)
        db.session.add(new_book)
        db.session.commit()

    def readFromBook(self):
        with app.app_context():
            result = db.session.execute(db.select(Book).order_by(Book.title))
            all_books = result.scalars()

     def readByQuery(self):
         with app.app_context():
             book = db.session.execute(db.select(Book).where(Book.title == "Harry Porter")).scalar()

      def updateBook(self):
          with app.app_context():
              book_to_update = db.session_execute(db.select(Book).where(Book.title == "Harry Potter")).scalar
              book_to_update.title = "Harr Potter"
            db.session.commit()
@app.route('/')
def get_all_posts():
    return render_template("index.html")

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/tempates/register.html",methods=["POST"])
def register():
    name=request.form["name"]
    surname = request.form["surname"]
    username = request.form["surname"]
    password= request.form["password"]




@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)



def connecttoSQLLiteDB():
    db = sqlite3.connect("book-collection.db")
    cursor = db.cursor()

def createTableFromDB():
    db = sqlite3.connect("book-collection.db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE books(id INTEGER PRIMARY KEY,title varchar(250) NOT NULL UNIQUE"
                   "author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
    db.commit()

def insertIntoDB():
    db = sqlite3.connect("book-collection.db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO books VALUES(1,'Harry Porter','J.K Rowling','9.3')")
    db.commit()





