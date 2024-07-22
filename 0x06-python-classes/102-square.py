#!/usr/bin/python3

class Square:
    """Represents a square with a given size."""

    def __init__(self, size=0):
        """
        Initializes a new Square instance.
        
        Args:
            size (float or int): The size of the square. Default is 0.
            
        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        
        Returns:
            float: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        
        Args:
            value (float or int): The new size of the square.
            
        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.
        
        Returns:
            float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compares if two squares are equal based on area.
        
        Args:
            other (Square): The other square to compare.
            
        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compares if two squares are not equal based on area.
        
        Args:
            other (Square): The other square to compare.
            
        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Compares if the current square is less than the other based on area.
        
        Args:
            other (Square): The other square to compare.
            
        Returns:
            bool: True if the current square's area is less than the other, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compares if the current square is less than or equal to the other based on area.
        
        Args:
            other (Square): The other square to compare.
            
        Returns:
            bool: True if the current square's area is less than or equal to the other, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Compares if the current square is greater than the other based on area.
        
        Args:
            other (Square): The other square to compare.
            
        Returns:
            bool: True if the current square's area is greater than the other, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compares if the current square is greater than or equal to the other based on area.
        
        Args:
            other (Square): The other square to compare.
            
        Returns:
            bool: True if the current square's area is greater than or equal to the other, False otherwise.
        """
        return self.area() >= other.area()

