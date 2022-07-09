#!/usr/bin/python3
"""
defines json representation of an object
"""
import json


def to_json_string(my_obj):
    """
    :param my_obj: object to return its JSON representation
    :return: the JSON representation of a string object
    """
    return json.dumps(my_obj)
