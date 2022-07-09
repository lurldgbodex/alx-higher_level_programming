#!/usr/bin/python3
"""
returns an object represented by Json string
"""
import json


def from_json_string(my_str):
    """
    :param my_str: object to return from JSON representation
    :return: from JSON representation to a string object
    """
    return json.loads(my_str)
