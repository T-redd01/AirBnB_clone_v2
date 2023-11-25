#!/usr/bin/python3
""" State Module for HBNB project """
from models import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel):
    """ object for amenities
        
        Attributes:
            __tablename__: name of table
            name: name of amenity
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        # need to create many to many relationship here wiht place
    else:
        name = ""
