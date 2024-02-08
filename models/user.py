#!/usr/bin/python3
"""Importing standard modules and modules from our packages"""
from models.base_model import BaseModel

"""
This is a python class that models a user class but inherits from
the BaseModel class as the parent class
"""

class User(BaseModel):
    """
    This is a class modelling the user object for the AirBnB Clone project.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
