#!/usr/bin/python3
"""
Contains the definition of the funtion lookup.
"""


def lookup(obj):
    """Return a list of available attrbutes and methods of an object

    Args:
        obj (any): object whose attributes and methods are to be returned
    """

    return (dir(obj))
