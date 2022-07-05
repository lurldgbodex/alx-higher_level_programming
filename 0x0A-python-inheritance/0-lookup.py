#!/usr/bin/python3
"""Finds and return a list of available attributes
and methods of an object."""


def lookup(obj):
    """Returns the list of attributes and methods of obj."""

    return dir(obj)
