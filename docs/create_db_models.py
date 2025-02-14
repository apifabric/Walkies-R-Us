# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class DogWalker(Base):
    """description: Represents a dog walker employed by the business."""
    __tablename__ = 'dog_walker'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String)
    email = Column(String)
    hourly_rate = Column(Float)

class Client(Base):
    """description: Represents a client owning dogs that require walking."""
    __tablename__ = 'client'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String)
    email = Column(String)
    address = Column(String)

class Dog(Base):
    """description: Represents a dog belonging to a client."""
    __tablename__ = 'dog'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    breed = Column(String)
    age = Column(Integer)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)

class Walk(Base):
    """description: Represents a scheduled dog walking session."""
    __tablename__ = 'walk'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, default=datetime.datetime.now)
    duration = Column(Integer)  # Duration in minutes
    dog_walker_id = Column(Integer, ForeignKey('dog_walker.id'), nullable=False)
    completed = Column(Boolean, default=False)

class WalkLocation(Base):
    """description: Represents a location where a dog walk can take place."""
    __tablename__ = 'walk_location'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String)

class WalkSchedule(Base):
    """description: Represents an association between a walk and a dog."""
    __tablename__ = 'walk_schedule'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    walk_id = Column(Integer, ForeignKey('walk.id'), nullable=False)
    dog_id = Column(Integer, ForeignKey('dog.id'), nullable=False)

class Feedback(Base):
    """description: Represents feedback from a client about a walk."""
    __tablename__ = 'feedback'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    walk_id = Column(Integer, ForeignKey('walk.id'), nullable=False)
    rating = Column(Integer)  # Rating out of 5
    comments = Column(String)

class Payment(Base):
    """description: Represents a payment made by a client for dog walking services."""
    __tablename__ = 'payment'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.datetime.now)
# Create the SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite', echo=False)
Base.metadata.create_all(engine)

# Create a configured "Session" class and a session
Session = sessionmaker(bind=engine)
session = Session()

# Create sample data
dog_walkers = [
    DogWalker(first_name='Alice', last_name='Johnson', phone_number='555-1234', email='alice.j@dogwalkers.com', hourly_rate=15.0),
    DogWalker(first_name='Bob', last_name='Smith', phone_number='555-5678', email='bob.s@dogwalkers.com', hourly_rate=18.5)
]

clients = [
    Client(first_name='Chris', last_name='Doe', phone_number='555-8765', email='chris@email.com', address='123 Elm St'),
    Client(first_name='Dana', last_name='Parker', phone_number='555-4321', email='dana@parker.com', address='456 Oak St')
]

dogs = [
    Dog(name='Buddy', breed='Golden Retriever', age=5, client_id=1),
    Dog(name='Max', breed='Labrador', age=3, client_id=1),
    Dog(name='Bella', breed='Poodle', age=4, client_id=2)
]

walks = [
    Walk(date=datetime.datetime(2023, 10, 1, 9, 30), duration=60, dog_walker_id=1, completed=True),
    Walk(date=datetime.datetime(2023, 10, 2, 14, 0), duration=45, dog_walker_id=2, completed=False)
]

locations = [
    WalkLocation(name='Central Park', address='789 Central St'),
    WalkLocation(name='Riverside Park', address='101 River Rd')
]

walk_schedules = [
    WalkSchedule(walk_id=1, dog_id=1),
    WalkSchedule(walk_id=1, dog_id=2),
    WalkSchedule(walk_id=2, dog_id=3)
]

feedback = [
    Feedback(client_id=1, walk_id=1, rating=5, comments="Great service!"),
    Feedback(client_id=2, walk_id=2, rating=4, comments="Good, but the dog was a bit tired.")
]

payments = [
    Payment(client_id=1, amount=50.0),
    Payment(client_id=2, amount=70.0)
]

# Add instances to the session
session.add_all(dog_walkers + clients + dogs + walks + locations + walk_schedules + feedback + payments)

# Commit and close the session
session.commit()
session.close()
