#!/usr/bin/python3
"""Importing standard modules and modules from our packages"""
from models.base_model import BaseModel

"""
This is a python class that models a place class but inherits from
the BaseModel class as the parent class
"""


class place(BaseModel):
    """
    Creates a class named place for the AirBnB Clone project.
    """
    amenity_ids = []
    city_id = ""
    description = ""
    latitude = 0.0
    longitude = 0.0
    max_guest = 0
    name = ""
    number_rooms = 0
    number_bathrooms = 0
    price_by_night = 0
    user_id = ""
