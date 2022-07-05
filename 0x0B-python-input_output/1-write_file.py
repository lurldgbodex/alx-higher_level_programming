#!/usr/bin/python3
"""
Reads from a file
"""


def number_of_lines(filename=""):
    """
    counts the number 0f lines in filename.
    :param filename: name of the file
    :return: number of lines
    """

    count = 0

    with open(filename) as f:
        text = f.readlines()
        for word in text:
            count += 1

    return count
