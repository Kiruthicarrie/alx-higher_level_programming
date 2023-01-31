#!/usr/bin/python3
"""
Contains the definition of the function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class/class that inherited
       from a_class

    Args:
        obj (unknown): Object whose type is to be checked
        a_class (str): class that obj is suspected to be an instance of
    """

    if issubclass(type(obj), a_class) or isinstance(obj, a_class):
        return True
    return False
