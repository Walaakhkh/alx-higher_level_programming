#!/usr/bin/python3
# 1-square.py
"""
This module defines a class Square that defines a square
with a private instance attribute 'size'.
"""


class Square:
    """
    This class defines a square with a private instance attribute 'size'.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
