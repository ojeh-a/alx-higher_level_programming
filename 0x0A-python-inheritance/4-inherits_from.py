#!/usr/bin/python3
"""This module defines a function `inherits_from`"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a specified class

    Args:
        obj - object being checked
        a_class - the specified class
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
