#!/usr/bin/python3
'''This module defines tests'''
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    '''This class defines tests for the place class'''

    def test_review_attributes(self):
        '''
        This method defines tests for the attributes
        of the Review class
        '''
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
        self.assertIsInstance(review, BaseModel)
        self.assertIsInstance(review, Review)


if __name__ == '__main__':
    unittest.main()
