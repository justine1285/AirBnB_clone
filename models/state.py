#!/usr/bin/python3
"""Importing standard modules and modules from our packages"""
from models.base_model import BaseModel

"""
This is a python class that models a state class but inherits from
the BaseModel class as the parent class
"""


class State(BaseModel):
    """
    This is a class modelling the state object for the AirBnB Clone project.
    """
    name = ""
