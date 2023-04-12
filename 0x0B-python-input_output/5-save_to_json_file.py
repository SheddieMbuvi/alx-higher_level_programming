#!/usr/bin/python3
"""
writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """The function"""
    with open(filename, 'w') as a_file:
        new = json.dumps(my_obj)
        a_file.write(new)
