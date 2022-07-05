#!/usr/bin/python3
"""
Reads from a file 
"""


def read_file(filename=""):
    """
    Reads from filename and prints its contents

    :param filename: name of the file
    """

    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
