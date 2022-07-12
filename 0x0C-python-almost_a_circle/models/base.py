#!/usr/bin/python3
"""
A module to define the base class
"""


class Base:
    """
    A class to define the base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor to define the instance attribute id
        :param id: instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
