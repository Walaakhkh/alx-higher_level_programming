#!/usr/bin/python3
"""
Module to define a Square class with methods for calculating area and printing.
"""

class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square in a 2D space.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square in a 2D space.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character #.

        Prints an empty line if size is 0.
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Return a string representation of the square for printing.

        Returns:
            str: The square representation.
        """
        import io
        import sys
        buffer = io.StringIO()
        sys.stdout = buffer
        self.my_print()
        sys.stdout = sys.__stdout__
        return buffer.getvalue()

