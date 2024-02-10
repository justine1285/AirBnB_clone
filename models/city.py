#!/usr/bin/python3
"""Importing standard modules and modules from our packages"""
from models.base_model import BaseModel

"""
This is a python class that models a city class but inherits from
the BaseModel class as the parent class
"""


class City(BaseModel):
    """
    This is a class modelling the city object for the AirBnB Clone project.
    """
    name = ""
    state_id = ""
