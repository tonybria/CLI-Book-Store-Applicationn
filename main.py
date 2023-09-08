from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .author import Author, Base  # Use relative import
from .genre import Genre  # Use relative import
from .book import Book  # Use relative import

# Create the Base class and database engine
engine = create_engine('sqlite:///bookstore.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

# Rest of your application logic (add_book, display_books, etc.) can go here.
# Import Author, Genre, and Book classes as needed.
