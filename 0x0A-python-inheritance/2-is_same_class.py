#!/usr/bin/python3
'''Module for is_same_class method'''


def is_same_class(obj, a_class):
     """
    Returns True if the object is exactly an instance of the specified class;
    otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) == a_class
