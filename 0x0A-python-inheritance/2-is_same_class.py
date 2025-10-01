#!/usr/bin/python3
"""This module defines a function `is_same_class`"""


def is_same_class(obj, a_class):
    """checks if an object is exactly and instance
        of a specified class
    Args:
        obj - object being checked
        a_class - class
    Returns: True or False
    """
    if type(obj) == a_class:
        return True
    return False
