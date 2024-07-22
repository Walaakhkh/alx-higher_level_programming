#!/usr/bin/python3
# 6-square.py
"""
This module defines a class Square that represents a square with private
instance attributes 'size' and 'position'.
"""

class Square:
    """
    This class defines a square with private instance attributes 'size' and 'position'.
    
    The size of the square must be an integer greater than or equal to 0.
    The position attribute must be a tuple of two positive integers.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance with the given size and position.
        
        Args:
            size (int): The size of the square, must be an integer >= 0.
            position (tuple): A tuple of two positive integers representing the position.
        
        Raises:
            TypeError: If size is not an integer or if position is not a tuple of two positive integers.
            ValueError: If size is less than 0 or if any value in position is negative.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves the position of the square.
        
        Returns:
            tuple: A tuple of two positive integers representing the position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.
        
        Args:
            value (tuple): A tuple of two positive integers representing the position.
        
        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                any(i < 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character '#'.
        
        If the size is 0, prints an empty line. The position attribute is used to
        determine the number of spaces to prepend to each line of the square.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)

