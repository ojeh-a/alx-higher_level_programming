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
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
