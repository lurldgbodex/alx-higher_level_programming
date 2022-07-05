#!/usr/bin/python3
"""Defines a class checking function."""


def is_same_class(obj, a_class):
    """
    function to determine if obj is an inherited instance of a_class
    :param obj: object to check
    :param a_class: class to verify the instance of
    :return: True if obj is an instance of a_class; false otherwise
    """

    return isinstance(obj, a_class) and type(obj) != a_class
