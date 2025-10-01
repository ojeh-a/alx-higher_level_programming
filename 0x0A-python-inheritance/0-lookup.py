"""Defines a function that returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """Lists all all available attributes
    and methods of an object passed to it

    Args:
        obj - object
    """
    return dir(obj)
