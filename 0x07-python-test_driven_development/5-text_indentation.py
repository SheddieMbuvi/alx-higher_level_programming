#!/usr/bin/python3
"""
Imports no module
"""


def text_indentation(text):
    """Function printing a text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for ch in text:
        if ch == "." or ch == "?" or ch == ":":
            print(ch, end="")
            print("\n")
        else:
            print(ch, end="")
