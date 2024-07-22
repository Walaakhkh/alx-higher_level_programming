#!/usr/bin/python3
import math

class MagicClass:
    """Represents a circle with a given radius."""

    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance.

        Args:
            radius (float or int): The radius of the circle.

        Raises:
            TypeError: If radius is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius

