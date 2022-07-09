#!/usr/bin/python3
"""
defines a json file object.
"""
import json


def load_from_json_file(filename):
    """
    :param filename: name of the file
    """
    with open(filename) as f:
        return json.load(f)
