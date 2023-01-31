#!/usr/bin/python3
"""
Contains the definition for the class MyList that inherits from list.
"""


class MyList(list):
    """Definition of class MyList that inherits from class list."""

    def print_sorted(self):
        """Prints list sorted in ascending order, assuming elements are int"""

        print(sorted(self))
