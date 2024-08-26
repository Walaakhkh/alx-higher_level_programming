#!/usr/bin/python3



def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object."""
    # Dictionary to hold serializable attributes
    result = {}

    # Loop over the attributes of the object
    for attr in dir(obj):
        # Skip private attributes and methods
        if not attr.startswith("__"):
            value = getattr(obj, attr)
            # Check if value is serializable
            if isinstance(value, (int, str, bool, list, dict)):
                result[attr] = value

    return result
