#!/usr/bin/python3
"""
Contains definition of the empty class BaseGeometry
"""


class BaseGeometry():
    """Definition of class BaseGeometry"""

    def area(self):
        """Raise an Exception with message 'area() is not implemented'"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates 'value' to be an integer greater than 0.

        Args:
            name (str): name of the value
            value (unknown): to be validated

        Raises:
            TypeError - if value is not an integer
            ValueErrror - if value is <= 0
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
