#!/usr/bin/python3
"""
Contains the definition of the function is_same_class
"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class.

    Args:
        obj (unknown): Object whose type is to be checked
        a_class (str): class that obj is suspected to be an instance of
    """

    if type(obj) == a_class:
        return True
    return False
