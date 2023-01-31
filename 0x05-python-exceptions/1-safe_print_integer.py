#!/usr/bin/python3


def safe_print_integer(value):
    """Print value with {:d}.format() format specifier and handle any ValueError
       exceptions.

    """
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
