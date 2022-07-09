#!/usr/bin/python3
"""appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """
    function appends a string at the end of a text file(UTF8)
    :param filename: name of the file
    :param text: text to append
    :return: number of characters added.
    """

    with open(filename, "a", encoding="utf-8") as myfile
        return myfile.append(text)
