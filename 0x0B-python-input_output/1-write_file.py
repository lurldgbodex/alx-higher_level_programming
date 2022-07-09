#!/usr/bin/python3
"""
writes to a file
"""


def write_file(filename=""):
    """
    writes a string to a textfile.
    :param filename: name of the file
    :return: number of characters written
    """

    with open(filename, "w", encoding="utf-8") as f:
        text = f.write()
