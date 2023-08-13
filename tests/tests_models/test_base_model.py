#!/usr/bin/python3
"""Test cases for base model"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Outlines various test cases for the class attributes and mehtods"""

    def setUp(self):
        self.user1 = BaseModel()
        self.user2 = BaseModel()

    def test_unique_id(self):
        self.assertNotEqual(self.user1.id, self.user2.id)

    def test_created_at(self):
        self.assertIsInstance(self.user1.created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.user1.updated_at, datetime)

    def test_save(self):
        self.user1.save()
        self.assertNotEqual(self.user1.updated_at, self.user1.created_at)

    def test_to_dict(self):
        new_dict = self.user2.to_dict()
        self.assertIsInstance(new_dict, dict)
        self.assertIn("created_at", new_dict)
        self.assertIn("updated_at", new_dict)
        self.assertIn("__class__", new_dict)
        self.assertIn("id", new_dict)
        self.assertNotIn("ifiok", new_dict)
        self.assertNotIn("kk", new_dict)

    def test_str(self):
        string_rep = str(self.user1)
        self.assertIsInstance(string_rep, str)
