#!/usr/bin/python3
"""Defines an empty geometry class."""


class BaseGeometry:
    """An empty geometry class"""

    def area(self):
        """Raises area not implemented exception"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        function validates value
        :param name: a string of name
        :param value: value to validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
