#!/usr/bin/python3
'''This module defines tests for the State class'''
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    '''
    This class defines tests for the state class
    '''

    def test_state_attributes(self):
        '''
        Tests for the attributes and class
        name of the state instance
        '''
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")
        self.assertIsInstance(state, BaseModel)
        self.assertIsInstance(state, State)


if __name__ == '__main__':
    unittest.main()
