#!/usr/bin/python3
"""
Contains definition of class MyInt
"""


class MyInt(int):
    """Defintion of class MyInt that inherits from class int"""

    def __eq__(self, other):
        """Return True when objects are not equal"""
        return self.real != other.real

    def __ne__(self, other):
        """Return True when objects are equal"""
        return self.real == other.real
