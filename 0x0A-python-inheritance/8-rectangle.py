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
        super().integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        raise Exception("area() is not implemented")
