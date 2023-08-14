#!/usr/bin/python3
"""Test cases for base model"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Outlines various test cases for the class attributes and mehtods"""

    def setUp(self):
        '''This is a setup method for creating instances
        to conduct test comparisons'''

        self.base_model1 = BaseModel()
        self.base_model2 = BaseModel()
        self.base_model_dict_1 = {
            'id': self.base_model1.id,
            'created_at': self.base_model1.created_at.isoformat(),
            'updated_at': self.base_model1.updated_at.isoformat(),
            '__class__': 'BaseModel'
            }

        self.base_model_dict_2 = {
                'id': self.base_model2.id,
                'created_at': self.base_model2.created_at.isoformat(),
                'updated_at': self.base_model2.updated_at.isoformat(),
                '__class__': 'BaseModel'
                }
        self.new_dict_1 = self.base_model1.to_dict()
        self.new_dict_2 = self.base_model2.to_dict()
        self.base_model_from_dict_1 = BaseModel(**self.new_dict_1)
        self.base_model_from_dict_2 = BaseModel(**self.new_dict_2)

    def test_unique_id(self):
        '''Test for uniqueness of the instance id's'''
        self.assertNotEqual(self.base_model1.id, self.base_model2.id)

    def test_created_at(self):
        ''' Test for the data type of the created @ attribute '''
        self.assertIsInstance(self.base_model1.created_at, datetime)

    def test_updated_at(self):
        ''' Test for the data type of the updated @ attribute '''
        self.assertIsInstance(self.base_model2.updated_at, datetime)

    def test_save(self):
        ''' Test for save method '''
        self.base_model1.save()
        self.assertNotEqual(
                self.base_model1.updated_at, self.base_model1.created_at
                )

    def test_to_dict(self):
        '''Test for serializing an object instance'''
        self.assertIsInstance(self.new_dict_1, dict)
        self.assertIsInstance(self.new_dict_2, dict)
        self.assertIn("created_at", self.new_dict_1)
        self.assertIn("created_at", self.new_dict_2)
        self.assertIn("updated_at", self.new_dict_1)
        self.assertIn("updated_at", self.new_dict_2)
        self.assertIn("__class__", self.new_dict_1)
        self.assertIn("__class__", self.new_dict_2)
        self.assertIn("id", self.new_dict_1)
        self.assertIn("id", self.new_dict_2)
        self.assertNotIn("ifiok", self.new_dict_1)
        self.assertNotIn("kk", self.new_dict_2)
        self.assertEqual(self.base_model_dict_1, self.new_dict_1)
        self.assertEqual(self.base_model_dict_2, self.new_dict_2)

    def test_str(self):
        ''' Test for the string representation of the instance'''
        string_rep = str(self.base_model1)
        self.assertIsInstance(string_rep, str)

    def test_from_dict(self):
        '''Test for de-serializing an instance'''
        self.assertEqual(
                self.base_model1.id, self.base_model_from_dict_1.id
                )
        self.assertEqual(
                self.base_model2.id, self.base_model_from_dict_2.id
                )
        self.assertEqual(
                self.base_model1.created_at,
                self.base_model_from_dict_1.created_at
                )
        self.assertEqual(
                self.base_model2.created_at,
                self.base_model_from_dict_2.created_at
                )
        self.assertEqual(
                self.base_model1.updated_at,
                self.base_model_from_dict_1.updated_at
                )
        self.assertEqual(
                self.base_model2.updated_at,
                self.base_model_from_dict_2.updated_at
                )
        self.assertIsInstance(self.base_model_from_dict_1.created_at, datetime)
        self.assertIsInstance(self.base_model_from_dict_2.created_at, datetime)
        self.assertIsInstance(self.base_model_from_dict_1.updated_at, datetime)
        self.assertIsInstance(self.base_model_from_dict_2.updated_at, datetime)
        self.assertIs(type(self.base_model_from_dict_1), BaseModel)
        self.assertIs(type(self.base_model_from_dict_2), BaseModel)
        '''
        self.assertNotIn("__class__", self.base_model_from_dict_1.values())
        self.assertNotIn("__class__", self.base_model_from_dict_2.values())
        '''


if __name__ == '__main__':
    unittest.main()
