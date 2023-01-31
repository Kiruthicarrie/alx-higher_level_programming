#!/usr/bin/python3
"""
Contains definition of class Rectangle that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Definition of class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize an instance of class Rectangle"""

        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of an instance of class Rectangle"""
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height)
