#!/usr/bin/python3
'''Module for lookup method'''


def lookup(obj):
    """Return a list of available attributes and methods of an object.

    Args:
        obj (object): The object whose attributes and methods are to be listed.

    Returns:
        list: A list of attributes and methods of the object.
    """
    return dir(obj)
