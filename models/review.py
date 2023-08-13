#!/usr/bin/python3
"""This module defines a class `Review`"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Provides user about other's experience of a place"""
    place_id = ""
    user_id = ""
    text = ""
