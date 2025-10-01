#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited.

    Args:
        obj: The object to check.
        a_class: Class to match the type of object to.
    Return:
        True or False.
    """
    if isinstance(obj, a_class):
        return True
    return False
