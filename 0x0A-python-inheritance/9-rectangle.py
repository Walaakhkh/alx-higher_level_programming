#!/usr/bin/python3
'''Module for Rectangle class.'''
BaseGeometry = _import_('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A subclass representing a rectangle.'''
    def _init_(self, width, height):
        '''Constructor.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Method which returns area of rectangle.'''
        return self._width * self._height

    def _str_(self):
        '''String representation method.'''
        return "[Rectangle] " + str(self._width) + "/" + str(self._height)
