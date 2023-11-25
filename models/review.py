#!/usr/bin/python3
""" Review module for the HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey


class Review(BaseModel):
    """ Review classto store review information

        Attributes:
           __tablename__: nmae of table
           text: to be explained
           place_id: foreign key to place
           user_id: forign key to user
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60),
                          ForeignKey("places.id"),
                          nullable=False)
        user_id = Column(String(60),
                         ForeignKey("users.id"),
                         nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
