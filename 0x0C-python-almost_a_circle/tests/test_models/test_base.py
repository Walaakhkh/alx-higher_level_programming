#!/usr/bin/python3

import unittest
import sys
import os

# Add the parent directory of models to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from models.base import add

class TestBase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
