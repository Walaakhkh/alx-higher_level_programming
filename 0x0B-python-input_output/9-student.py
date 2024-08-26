#!/usr/bin/python3
""" Module defining the Student class.
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

    def to_json(self):
        """ Retrieves a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary representation of the student's attributes.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
