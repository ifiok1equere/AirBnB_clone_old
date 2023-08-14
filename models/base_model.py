#!/usr/bin/python3
"""This module contains the parent class"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
        This represents the parent classs
        It defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        '''
        This method initializes attributes for the base model class
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for attr, value in kwargs.items():
                if attr == "__class__":
                    continue
                elif attr == "created_at" or attr == "updated_at":
                    new_attr_value = datetime.fromisoformat(kwargs[attr])
                    setattr(self, attr, new_attr_value)
                else:
                    setattr(self, attr, value)
            storage.new(self)
        else:
            """self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()"""
            storage.new(self)

    def __str__(self):
        '''
        This magic method is the string representation of the
        base model class
        '''
        cls_name = self.__class__.__name__
        self_id = self.id
        return "[{:s}] ({}) {}".format(cls_name, self_id, self.__dict__)

    def save(self):
        '''
        This method updates the instance attribute "updated_at"
        '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''
        This method returns all key/value pairs of the class __dict__ instance
        as well as a new key call '__class__' whose value is the class name.
        '''
        to_dict = {"__class__": self.__class__.__name__}
        to_dict.update(self.__dict__)
        new_dict = {
                "created_at": to_dict["created_at"].isoformat(), "updated_at":
                to_dict["updated_at"].isoformat()
                }
        to_dict.update(new_dict)
        return to_dict
