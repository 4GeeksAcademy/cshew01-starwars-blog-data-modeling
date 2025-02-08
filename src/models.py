import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    email = Column(String(30), nullable=False, unique=True)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    category = Column(String(15), nullable=False)
    category_id = Column(Integer, nullable=False)
    item = Column(String(30), nullable=False)
    item_id = Column(Integer, nullable=False)

class Starships(Base):
    __tablename__ = 'starships'
    uid = Column(Integer, ForeignKey('favorites.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('favorites.id'), nullable=False)
    name = Column(String(30), nullable=False)
    model = Column(String(30), nullable=False)
    starship_class = Column(String(30), nullable=False)
    cost_in_credits = Column(String(30), nullable=False)
    crew = Column(String(30), nullable=False)
    hyperdrive_rating = Column(String(30), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    uid = Column(Integer, ForeignKey('favorites.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('favorites.id'), nullable=False)
    name = Column(String(30), nullable=False)
    diameter = Column(String(15), nullable=False)
    rotation_period = Column(String(15), nullable=False)
    orbital_period = Column(String(15), nullable=False)
    population = Column(String(20), nullable=False)
    climate = Column(String(15), nullable=False)
    terrain = Column(String(15), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    uid = Column(Integer, ForeignKey('favorites.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('favorites.id'), nullable=False)
    name = Column(String(30), nullable=False)
    birth_year = Column(String(30), nullable=False)
    gender = Column(String(30), nullable=False)
    homeworld_id = Column(Integer, ForeignKey('planets.uid'), nullable=False)
    starships_id = Column(Integer, ForeignKey('starships.uid'), nullable=False)    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
