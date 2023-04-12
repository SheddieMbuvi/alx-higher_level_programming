#!/usr/bin/python3
"""
From json to normal string
"""
import json


def from_json_string(my_str):
    """The fundtion"""
    newstr = json.loads(my_str)
    return newstr
