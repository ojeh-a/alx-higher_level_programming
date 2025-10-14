#!/usr/bin/python3
"""This module defines the function `read_file`"""


def read_file(filename=""):
    """Read and print the content of `filename` to stdout"""

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
