from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    author_name = Column(String)

# Add relationships in the Author table
Author.books = relationship("Book", order_by="Book.id", back_populates="author")
