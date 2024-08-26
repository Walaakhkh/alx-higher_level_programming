#!/usr/bin/python3
""" Module defining the Student class with serialization and deserialization.
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
            attrs (list, optional): List of attribute names to
            include in the dictionary.

        Returns:
            dict: A dictionary representation of the student's attributes.
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }

        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)

        return result

    def reload_from_json(self, json):
        """ Updates the Student instance attributes from a given dictionary.

        Args:
            json (dict): A dictionary with attribute names as keys and their
            values."""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
