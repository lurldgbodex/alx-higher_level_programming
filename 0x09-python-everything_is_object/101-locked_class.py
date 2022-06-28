#!/usr/bin/python3
"""
Module 101-locked_class
creates a class LockedClass with no class or object attribute
"""


class LockedClass:
    """A class with no object or class attrubute and prevents user from dynamicall creating new instance attribute"""

    __slots__ = ['first_name']


    def __init__(self, first_name=):
    """"A method that instances the firstname attribute"""
        self.first_name = first_name
