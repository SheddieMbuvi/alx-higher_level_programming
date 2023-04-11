#!/usr/bin/python3
"""
Checks if it same or from inherited class
"""


def is_kind_of_class(obj, a_class):
    """method to check the similarity"""
    if isinstance(obj, a_class):
        return True
    return False
