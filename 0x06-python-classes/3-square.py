#!/usr/bin/python3
# 3-square.py
"""
This module defines a class Square that defines a square
with a private instance attribute 'size'.
"""


class Square:
    """
    This class defines a square with a private instance attribute 'size'.

    The size of the square must be an integer greater than or equal to 0.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square, must be an integer >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
