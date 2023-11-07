#!/usr/bin/python3
"""Defines a function read_file that readsa text file
    and prints it to standard output.
"""


def read_file(filename=""):
    """Prints the contents of a file with UTF8 encoding"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
