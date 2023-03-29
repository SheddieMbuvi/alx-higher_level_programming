#!/usr/bin/python3
"""
No import modules allowed for this
"""


class Square:
    """Class that defines the size"""
    def __init__(self, size=0):
        """Method for initialization"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
