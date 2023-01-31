#!/usr/bin/python3
"""
Contains definition of a function add_attribute
"""


def add_attribute(obj, name, value):
    """Adds an attribute to an object and raises an error if not possible

    Args:
        obj (Object): name of object to add attribute to
        name (str): name of attribute to add
        value (any): value of attribute to be added

    Raises:
        TypeError: if attribute can't be added to obj
    """

    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
