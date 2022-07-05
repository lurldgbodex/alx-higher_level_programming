#!/usr/bin/python3
"""Defines an empty geometry class."""


class BaseGeometry:
    """An empty geometry class"""

    def area(self):
        """Raises area not implemented exception"""

        raise Exception('area() is not implemented')
