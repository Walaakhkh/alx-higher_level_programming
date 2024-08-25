#!/usr/bin/python3
"""
Contains the class MyInt
"""


class MyInt(int):
    """rebel version of an integer, perfect for opposite day!"""
    def _new_(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls)._new_(cls, *args, **kwargs)

    def _eq_(self, other):
        """what was != is now =="""
        return int(self) != other

    def _ne_(self, other):
        """what was == is now !="""
        return int(self) == other
