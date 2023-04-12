#!/usr/bin/python3
"""
String to To JSON string with json import
"""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation"""
    return json.dumps(my_obj)
