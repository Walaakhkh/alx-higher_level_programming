#!/usr/bin/python3

class Square:
    """Represents a square with a specific size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with size and position.

        Args:
            size (int): The size of the square.
            position (tuple): A tuple of 2 positive integers representing
            the position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: The size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """tuple: The position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If `value` is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
            not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character `#` considering its position.
        """
        if self.__size == 0:
            print()
            return

        # Print empty lines for vertical offset
        for _ in range(self.__position[1]):
            print()

        # Print each row of the square
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns the string representation of the square using `my_print()`.

        Returns:
            str: The string representation of the square.
        """
        import io
        import sys
        buffer = io.StringIO()
        sys.stdout = buffer
        self.my_print()
        sys.stdout = sys.__stdout__
        return buffer.getvalue()
