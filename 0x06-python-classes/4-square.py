#!/usr/bin/python3
# 4-square.py
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
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square, must be an integer >= 0.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
