#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_middle(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_all_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_values(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_max_with_duplicates(self):
        self.assertEqual(max_integer([1, 2, 3, 3]), 3)

    def test_string_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'three', 4])

if __name__ == '__main__':
    unittest.main()

