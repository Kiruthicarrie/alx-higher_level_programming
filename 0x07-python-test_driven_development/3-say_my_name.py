#!/usr/bin/python3
"""Contains definition of say_my_name() function"""


def say_my_name(first_name, last_name=""):
    """"Prints 'My name is <first_name> <last_name>'.

    Args:
        first_name (str): first name
        last_name (str, optional): last name, optional argument

    Returns:
        no return value
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name:
        print("My name is {} {}".format(first_name, last_name))
