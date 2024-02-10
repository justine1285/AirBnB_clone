#!/usr/bin/python3
"""Importing standard modules and modules from our packages"""
from models.base_model import BaseModel

"""
This is a python class that models an Amenity class but inherits from
the BaseModel class as the parent class
"""


class Amenity(BaseModel):
    """
    This is a class modelling the Amenity object for the AirBnB Clone project.
    """
    name = ""
