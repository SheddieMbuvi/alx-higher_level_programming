#!/usr/bin/python3
"""
No import modules for this function

add_integer(a, b)
"""


def add_integer(a, b=98):
    """Function that adds two integers
    >>> (4, 4)
    output 8
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
