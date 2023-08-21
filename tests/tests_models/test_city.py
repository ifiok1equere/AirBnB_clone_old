#!/usr/bin/python3
''' This module defines tests for the City Class'''

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    '''
    This class defines tests for the city class
    '''

    def test_city_attributes(self):
        '''
        This function defines tests for
        the attributes of the city class
        '''
        city1 = City()
        city2 = City()
        self.assertTrue(hasattr(city1, "state_id"))
        self.assertTrue(hasattr(city1, "name"))
        self.assertEqual(city2.state_id, "")
        self.assertEqual(city2.name, "")
        self.assertIsInstance(city1, BaseModel)
        self.assertIsInstance(city2, BaseModel)
        self.assertIsInstance(city1, City)
        self.assertIsInstance(city2, City)
        self.assertEqual(city1.name, city2.name)
        self.assertEqual(city1.state_id, city2.state_id)


if __name__ == '__main__':
    unittest.main()
