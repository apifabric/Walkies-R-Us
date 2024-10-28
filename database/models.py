# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 28, 2024 19:22:01
# Database: sqlite:////tmp/tmp.rIpC3GH6mA/Walkies-R-Us/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Client(SAFRSBaseX, Base):
    """
    description: Represents a client owning dogs that require walking.
    """
    __tablename__ = 'client'
    _s_collection_name = 'Client'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String)
    email = Column(String)
    address = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    DogList : Mapped[List["Dog"]] = relationship(back_populates="client")
    PaymentList : Mapped[List["Payment"]] = relationship(back_populates="client")
    FeedbackList : Mapped[List["Feedback"]] = relationship(back_populates="client")



class DogWalker(SAFRSBaseX, Base):
    """
    description: Represents a dog walker employed by the business.
    """
    __tablename__ = 'dog_walker'
    _s_collection_name = 'DogWalker'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String)
    email = Column(String)
    hourly_rate = Column(Float)

    # parent relationships (access parent)

    # child relationships (access children)
    WalkList : Mapped[List["Walk"]] = relationship(back_populates="dog_walker")



class WalkLocation(SAFRSBaseX, Base):
    """
    description: Represents a location where a dog walk can take place.
    """
    __tablename__ = 'walk_location'
    _s_collection_name = 'WalkLocation'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)



class Dog(SAFRSBaseX, Base):
    """
    description: Represents a dog belonging to a client.
    """
    __tablename__ = 'dog'
    _s_collection_name = 'Dog'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    breed = Column(String)
    age = Column(Integer)
    client_id = Column(ForeignKey('client.id'), nullable=False)

    # parent relationships (access parent)
    client : Mapped["Client"] = relationship(back_populates=("DogList"))

    # child relationships (access children)
    WalkScheduleList : Mapped[List["WalkSchedule"]] = relationship(back_populates="dog")



class Payment(SAFRSBaseX, Base):
    """
    description: Represents a payment made by a client for dog walking services.
    """
    __tablename__ = 'payment'
    _s_collection_name = 'Payment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    client_id = Column(ForeignKey('client.id'), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(DateTime)

    # parent relationships (access parent)
    client : Mapped["Client"] = relationship(back_populates=("PaymentList"))

    # child relationships (access children)



class Walk(SAFRSBaseX, Base):
    """
    description: Represents a scheduled dog walking session.
    """
    __tablename__ = 'walk'
    _s_collection_name = 'Walk'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    duration = Column(Integer)
    dog_walker_id = Column(ForeignKey('dog_walker.id'), nullable=False)
    completed = Column(Boolean)

    # parent relationships (access parent)
    dog_walker : Mapped["DogWalker"] = relationship(back_populates=("WalkList"))

    # child relationships (access children)
    FeedbackList : Mapped[List["Feedback"]] = relationship(back_populates="walk")
    WalkScheduleList : Mapped[List["WalkSchedule"]] = relationship(back_populates="walk")



class Feedback(SAFRSBaseX, Base):
    """
    description: Represents feedback from a client about a walk.
    """
    __tablename__ = 'feedback'
    _s_collection_name = 'Feedback'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    client_id = Column(ForeignKey('client.id'), nullable=False)
    walk_id = Column(ForeignKey('walk.id'), nullable=False)
    rating = Column(Integer)
    comments = Column(String)

    # parent relationships (access parent)
    client : Mapped["Client"] = relationship(back_populates=("FeedbackList"))
    walk : Mapped["Walk"] = relationship(back_populates=("FeedbackList"))

    # child relationships (access children)



class WalkSchedule(SAFRSBaseX, Base):
    """
    description: Represents an association between a walk and a dog.
    """
    __tablename__ = 'walk_schedule'
    _s_collection_name = 'WalkSchedule'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walk_id = Column(ForeignKey('walk.id'), nullable=False)
    dog_id = Column(ForeignKey('dog.id'), nullable=False)

    # parent relationships (access parent)
    dog : Mapped["Dog"] = relationship(back_populates=("WalkScheduleList"))
    walk : Mapped["Walk"] = relationship(back_populates=("WalkScheduleList"))

    # child relationships (access children)
