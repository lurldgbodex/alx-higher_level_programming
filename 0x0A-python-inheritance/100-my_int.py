#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, other):
        """returns inequality"""

        return super().__ne__(other)

    def __ne__(self, other):
        """returns euality"""

        return super().__eq__(other)
