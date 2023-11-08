#!/usr/bin/python3
"""Defines a class Students"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name: The student's first name.
            last_name: The student's last name.
            age: The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """Get a dictionary representation of the student."""
            return self.__dict__
