#!/bin/usr/python3
""" A function that adds 2 integers."""

def add_integer(a, b=98):
    """ function adds 2 integers: a and b.
    a and b must be an integer or float
    """

    if type(a) is not int or type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")
    
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
