#!/usr/bin/python3
class LockedClass:
    """A class that only allows dynamic creation of the
    'first_name' attribute."""
    
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        """Set an attribute if it is 'first_name'; otherwise, raise an
        AttributeError."""
        if name == 'first_name':
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no
            attribute '{name}'")
