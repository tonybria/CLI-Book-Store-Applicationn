import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)

engine = create_engine('sqlite:///bookstore.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

# Function to add a book to the database
def add_book(session):
    title = input("Enter the title of the book: ")
    author = input("Enter the author's name: ")
    genre = input("Enter the genre of the book: ")

    book = Book(title=title, author=author, genre=genre)
    session.add(book)
    session.commit()
    print("Book added successfully!")

# Function to display all books in the database
def display_books(session):
    books = session.query(Book).all()
    if not books:
        print("No books found in the database.")
    else:
        for book in books:
            print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}")

# Function to search for a book by title
def search_book(session):
    title_to_search = input("Enter the title of the book to search for: ")
    try:
        book = session.query(Book).filter_by(title=title_to_search).one()
        print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}")
    except NoResultFound:
        print(f"Book with title '{title_to_search}' not found.")

# Function to delete a book by title
def delete_book(session):
    title_to_delete = input("Enter the title of the book to delete: ")
    try:
        book = session.query(Book).filter_by(title=title_to_delete).one()
        session.delete(book)
        session.commit()
        print(f"Book '{title_to_delete}' deleted successfully.")
    except NoResultFound:
        print(f"Book with title '{title_to_delete}' not found.")

def main():
    session = Session()

    while True:
        print("\nLatto's Book Store Application")
        print("1. Add a Book")
        print("2. Display Books")
        print("3. Search for a Book")
        print("4. Delete a Book")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            add_book(session)
        elif choice == '2':
            display_books(session)
        elif choice == '3':
            search_book(session)
        elif choice == '4':
            delete_book(session)
        elif choice == '5':
            print("Thank you for using Latto's Book Store Application. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key = True)
    name = Column(String)
class Genre(Base):
    __tablename__ = "genre"
    
    id = Column(Integer, primary_key = True)
    name  = Column(String)




if __name__ == "__main__":
    main()
