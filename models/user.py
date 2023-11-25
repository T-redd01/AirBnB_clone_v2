#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
from models import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    ''' Definition of the User class

        Attributes:
            __tablename__: name of table
            email: user email
            password: user password
            first_name: user first name
            last_name: user last name
            places: places user has been
            reviews: reviews user has made
    '''
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user",
                          cascade="all, delete-orphan")
    reviews = relationship("Review", backref="user",
                           cascade="all, delete-orphan")
