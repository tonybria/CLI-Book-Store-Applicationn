from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    genre_name = Column(String)

# Add relationships in the Genre table
Genre.books = relationship("Book", order_by="Book.id", back_populates="genre")
