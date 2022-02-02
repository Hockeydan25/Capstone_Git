"""
Dan Smestad ITEC 2905-80 Capstone 2/2/2021.
Python testing example for testing your code. 

"""
import unittest
from unittest import TestCase

import quote

class QuoteTest(TestCase):

    def test_quote_for_small_lawn_same_day(self):
        actual_quote = quote.lawn_quote('small', True)
        expected_quote = 15
        self.assertEqual(expected_quote, actual_quote)

    def test_quote_for_large_lawn_not_same_day(self):
        actual_quote = quote.lawn_quote('large', False)
        expected_quote = 20
        self.assertEqual(expected_quote, actual_quote)

    def test_quote_for_unrecognized_size(self):
        actual_quote = quote.lawn_quote('hockey', False)
        self.assertIsNone(actual_quote)  
        # does same (as commented out code) shorter with us of internal function. 

        # expected_quote = None
        # self.assertEqual(expected_quote, actual_quote)    



if __name__ == '__main__':  #clara question. How does this work?
    unittest.main()
