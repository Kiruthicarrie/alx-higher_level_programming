#!/usr/bin/python3
"""
Contains the definition of the function inherits_from
"""


def inherits_from(obj, a_class):
    """Returns True if obj is instance of a class that inherited from a_class

    Args:
        obj (unknown): Object whose type is to be checked
        a_class (str): class that obj is suspected to be an instance of
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
