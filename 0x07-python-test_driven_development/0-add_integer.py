#!/usr/bin/python3
""" Define add_integer function """


def add_integer(a, b=98):
    """ Return the sum of two integers or float.

    Numbers are first casted into integer if they float.

    Raises:
        TypeError: If a or b are neither int nor float.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
