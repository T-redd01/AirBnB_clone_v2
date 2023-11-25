#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class for state objects

        Attributes:
            __tablename__: name of table
            name: name of state
            cities: represent relationship between city and state
    """
    __tablename__ = "states"
    if storage_type == "db":
        name = Column(String(128),
                      nullable=False)
        cities = relationship("City", backref="state",
                              cascade='all, delete, delete-orphan')
    else:
        name = ""
