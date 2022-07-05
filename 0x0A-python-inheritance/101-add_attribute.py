#!/usr/bin/python3
"""Defines a function that adds attributes to objects"""


def add_attribute(obj, att, value):
    """
    adds a new attribute to an object if possible
    :param obj: The object to add attribut to
    :param att: Name of the attribute to add to obj
    :param value: Value of att
    :raise TypeError if the attribute cannot be found
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribue")
    setattr(obj, att, value)
