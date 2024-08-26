#!/usr/bin/python3
""" Module for serializing class instances to JSON-compatible dictionaries.
"""

def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON
    serialization of an object.

    Args:
        obj: The object instance to serialize.

    Returns:
        A dictionary description of the object's attributes.
    """
    result = {}

    # Iterate through the attributes of the object
    for attr in dir(obj):
        # Skip attributes that start with "__" or are callable (methods)
        if not attr.startswith("__") and not callable(getattr(obj, attr)):
            value = getattr(obj, attr)
            # Check if the value is serializable
            if isinstance(value, (int, str, bool, list, dict)):
                result[attr] = value
    
    return result
