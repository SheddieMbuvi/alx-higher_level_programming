#!/usr/bin/python3
"""
Has no inport module
check if instance is same as sub class
"""


def inherits_from(obj, a_class):
    """check if instance is same as sub class"""
    if issubclass(obj.__class__, a_class) is True:
        if obj.__class__ is not a_class:
            return True
    return False
