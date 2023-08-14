#!/usr/bin/python3
''' This modules defines tests for the amenity class '''
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    '''
    This test defines the tests on the Amenity class
    '''

    def test_amenity_attributes(self):
        '''
        The test tests for the correctness of the
        attributes of the amenity instnace
        '''

        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
        self.assertIsInstance(amenity, BaseModel)
        self.assertIsInstance(amenity, Amenity)


if __name__ == '__main__':
    unittest.main()
