#!/usr/bin/python3
"""
Has no import module and appends text to file
"""


def append_write(filename="", text=""):
    """The function to append a text"""
    with open(filename, 'a') as a_file:
        newfile = a_file.write(text)
    return newfile
