#!/usr/bin/python3
"""Importing standard modules and modules from our packages"""
from models.base_model import BaseModel

"""
This is a python class that models a review class but inherits from
the BaseModel class as the parent class
"""

class Review(BaseModel):
    """
    This is a class modelling the Review object for the AirBnB Clone project.
    """
    place_id = ""
    user_id = ""
    text = ""
