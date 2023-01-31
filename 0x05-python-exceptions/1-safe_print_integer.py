#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))  # print given value
        return (True)  # return True if value is an integer
    except (TypeError, ValueError):  # catch value error exception
        return (False)  # return False
