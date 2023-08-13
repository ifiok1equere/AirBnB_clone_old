#!/usr/bin/python3
'''
This module creates an instance of the storage class
'''
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
