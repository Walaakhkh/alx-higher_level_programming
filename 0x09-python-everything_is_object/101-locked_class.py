#!/usr/bin/python3
class LockedClass:
    """
    LockedClass prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called `first_name`.

    Attributes:
        __slots__ (list): Defines a list of allowed attributes for instances.
                          In this case, only `first_name` is allowed.
    """

    __slots__ = ['first_name']

    def __init__(self):
        """
        Initialize the LockedClass with no attributes.
        """
        pass
