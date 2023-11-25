#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv


class Amenity(BaseModel, Base):
    """ object for amenities

        Attributes:
            __tablename__: name of table
            name: name of amenity
    """
    __tablename__ = "amenities"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        # need to create many to many relationship here wiht place
    else:
        name = ""
