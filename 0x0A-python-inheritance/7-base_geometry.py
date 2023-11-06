#!/usr/bin/python3
"""Defines an empty class BaseGeometry"""


class BaseGeometry:
    """Represent Base Geometry."""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This function validates value.

        Args:
            name: Always a string.
            value: Value to be validated.
        """
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
