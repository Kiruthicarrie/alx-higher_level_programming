#!/usr/bin/python3
"""
Contains definition for the class Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definition of class Square that inherits from class Rectangle"""

    def __init__(self, size):
        """Initialise an instance of the class Square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Return a string representation of an instance of class Square"""
        return "[{}] {}/{}".format(type(self).__name__, self.__size,
                                   self.__size)
