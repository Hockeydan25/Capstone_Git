"""
Dan Smestad ITEC 2905-80 Capstone 2/2/2021.
Python testing example for testing your code. 
Start your test functions with the word test!
don't forget assert mothods. Team testing is good!
"""
import unittest
from unittest import TestCase

import area

class TestShapeAreas(TestCase):

    def test_triangle_area(self):  # object. "test" should be first word and give you test methods. 
        self.assertEqual(10, area.triangle_area(4, 5))  # Assert equal check if two values are the same.

    def test_triangle_area_floating_point(self):  # object floating point test
        self.assertAlmostEqual(17.79875, area.triangle_area(7.25, 4.91))  
        # deciamls expecting? rounding causes error so we useassetAlmostEqual.
    def test_triangle_area_zero_value(self):  # object zero value point test
        self.assertEqual(0, area.triangle_area(0, 0))     

    # def test_triangle_area_negative_value(self):  # object neagative value point test
    #     self.assertLessEqual(-10, area.triangle_area(-4, -5))
    # this doesn't work now after the if statement in area.py  

    def test_negative_base_height_raises_error(self):  # object neagative value point test
        with self.assertRaises(ValueError):  # with context manager.
            area.triangle_area(-3, 0)  # no value error issue in first run if values aren't out of scope.
        # both base an height checks with the folling
        with self.assertRaises(ValueError):  # with context manager.
            area.triangle_area(0, -1)

        with self.assertRaises(ValueError):  # with context manager.
            area.triangle_area(-1, -1)    

    def test_base_height_zero(self):  # getting return test for zero
        self.assertEqual(0, area.triangle_area(0, 4)) 
        self.assertEqual(0, area.triangle_area(4, 0)) 
        self.assertEqual(0, area.triangle_area(0, 0)) 



if __name__ == '__main__':
    unittest.main()



"""
first message:
.  # . dot/period is equal to a passing test indication.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

second message:
.F # .= one test passed , F is the Fail test followed by error message.
======================================================================
FAIL: test_triangle_area_floating_point (test_area.TestShapeAreas)
"""