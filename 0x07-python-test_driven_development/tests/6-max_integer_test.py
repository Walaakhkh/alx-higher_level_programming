#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_positive_integers(self):
        """Test a list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([10, 20, 30, 40]), 40)

    def test_negative_integers(self):
        """Test a list with negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_integers(self):
        """Test a list with both positive and negative integers"""
        self.assertEqual(max_integer([-1, 0, 1, 2, 3]), 3)
        self.assertEqual(max_integer([-10, -20, 30, 40]), 40)
        self.assertEqual(max_integer([10, -20, 30, -40]), 30)

    def test_single_element(self):
        """Test a list with a single element"""
        self.assertEqual(max_integer([10]), 10)
        self.assertEqual(max_integer([-10]), -10)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_duplicate_max(self):
        """Test a list with duplicate maximum values"""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 4]), 4)

    def test_all_same_elements(self):
        """Test a list where all elements are the same"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_floats_and_integers(self):
        """Test a list with both floats and integers"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4]), 4)
        self.assertEqual(max_integer([-1.1, -2.2, 3.3, 2.2]), 3.3)

if __name__ == '__main__':
    unittest.main()
