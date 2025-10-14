#!/usr/bin/python3
"""Defines write_file function"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8).

    Args:
        filename: file name to write into
        text: strings to write into the file
    Return:
        The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        write = f.write(text)
        return write
