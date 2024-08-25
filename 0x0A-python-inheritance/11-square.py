#!/usr/bin/python3
'''Module for Rectangle class.'''
Rectangle = _import_('9-rectangle').Rectangle


class Square(Rectangle):
    '''A subclass representing a rectangle.'''
    def _init_(self, size):
        '''Constructor.'''
        self.integer_validator("size", size)
        self.__size = size
        super()._init_(size, size)

    def area(self):
        '''Method for area of square.'''
        return self.__size ** 2

    def _str_(self):
        '''Returns string representation of this square.'''
        return "[Square] " + str(self._size) + "/" + str(self._size)
