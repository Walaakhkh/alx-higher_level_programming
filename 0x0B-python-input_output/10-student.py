#!/usr/bin/python3
""" Module defining the Student class with customizable JSON serialization
"""


class Student:
    """ Defines a student by first_name, last_name, and age.
    """


    def __init__(self, first_name, last_name, age):
        """ Initializes the student with first_name, last_name, and age.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of the Student instance.
        If attrs is a list of strings, only attribute names contained in
        this list are retrieved.
        Otherwise, all attributes are retrieved.

        Args:
            attrs (list, optional): List of attribute names to include in the
            dictionary.

        Returns:
            dict: A dictionary representation of the student's attributes.
        """
        if attrs is None:
            # Return all attributes if no specific attributes are requested
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }

        # Handle case where attrs is provided
        result = {}
        for attr in attrs:
            # Only include attributes that exist in the instance
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)

        return result
