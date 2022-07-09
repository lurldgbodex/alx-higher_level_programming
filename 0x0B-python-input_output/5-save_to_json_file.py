#!/usr/bin/python3
"""
writes an object to a text file using json rep.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    :param my_obj: object to write to file in JSON representation
    :param filename: name of the file
    """
    json.dump(my_obj, filename)
