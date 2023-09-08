from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))  # Foreign key to Authors table
    genre_id = Column(Integer, ForeignKey('genres.id'))    # Foreign key to Genres table

    # Establish relationships with Author and Genre
    author = relationship("Author", back_populates="books")
    genre = relationship("Genre", back_populates="books")
