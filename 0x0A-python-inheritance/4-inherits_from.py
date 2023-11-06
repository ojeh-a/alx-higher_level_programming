#!/usr/bin/python3
"""Defines function inherits_from"""


def inherits_from(obj, a_class):
    """
    Checks if an object is inherited.

    Args:
        obj: object to check.
        a_class: The class to check if object is inherited from.
    Returns:
        True or False.
    """
    if not issubclass(type(obj), a_class) and type(obj) != a_class:
        return False
    return True
