#!/usr/bin/python3
"""This module defines a class `Amenity`"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines the amenities of available in a state"""
    name = ""
