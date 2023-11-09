#!/usr/bin/python3
"""Defines a add_attribute."""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object

    Args:
        obj: Object to add an attribute to.
        att: Attribute to add
        value: Value of att.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
