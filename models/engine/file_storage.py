#!/usr/bin/env python3
"""This module contains the file storage class"""
import os
import json
#from models.base_model import to_dict


class FileStorage:
    """Serializes instances to JSON file and vice versa"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """initializes objects with defined attributes"""
        pass

    def all(self):
        """returns a dicitonary of objects in `__objects`"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the `obj` with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes `__objects` to the JSON file"""
        obj_dict = {}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """Deserializes JSON to the `__objects`"""
        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
