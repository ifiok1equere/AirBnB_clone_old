#!/usr/bin/python3
"""This module defines a class `City`"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines the city of a user"""
    state_id = ""
    name = ""
