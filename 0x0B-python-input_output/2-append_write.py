#!/usr/bin/python3
"""Defines append_write"""


def append_write(filename='', text=''):
    """
    Appends a string at the end of a text file.

    Args:
        filename: The file to append to,
        text: what to append to a file.
    return: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
