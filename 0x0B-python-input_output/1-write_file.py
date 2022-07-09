#!/usr/bin/python3
"""
writes to a file
"""


def write_file(filename="", text=""):
    """
    writes a string to a textfile.
    :param filename: name of the file
    :param text: contains the string to write to file
    :return: number of characters written
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
