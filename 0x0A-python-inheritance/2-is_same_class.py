#!/usr/bin/python3
"""Defines a class checking function."""


def is_same_class(obj, a_class):
    """
    function to determine if obj is an instance of a_class
    :param obj: object to check
    :param a_class: class to verify the instance of
    :return: True if ogj is an instance of a_class; false otherwise
    """

    return True if type(obj) is a_class else False
