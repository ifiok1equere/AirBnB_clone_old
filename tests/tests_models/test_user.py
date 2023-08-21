#!/usr/bin/python3
''' This module tests a user '''
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    ''' This class tests for a user and it attributes '''

    def test_inheritance(self):
        '''This method tests for inheritance
        of the base model class
        '''
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        '''
        This method tests for the attributes
        of a user.
        '''
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
'''
if __name__ == '__main__':
    unittest.main()
'''
