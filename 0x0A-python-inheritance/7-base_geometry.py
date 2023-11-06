#!/usr/bin/python3
"""Module 7-base_geometry.
Creates s BaseGeometry class.
"""


class BaseGeometry:
    """Represent Base Geometry."""

    def area(self):
        """Raises an Exception with the message
        'area() is not implemented'.
        """
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
