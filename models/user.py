#!/usr/bin/python3
"""This module defines a class `User` that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines a class for a user that inherits from BaseModel super class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
