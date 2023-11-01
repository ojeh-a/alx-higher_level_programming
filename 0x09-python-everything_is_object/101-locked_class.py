#!/usr/bin/python3
"""Define class LockedClass."""


class LockedClass:
    """
    Prevent user from dynamically creating creating new attribute
    except the attribute is "first_name"
    """

    __slots__ = ("first_name")
