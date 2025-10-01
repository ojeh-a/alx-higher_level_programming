#!/usr/bin/python3
"""Define MyList that inherits from list.
"""


class MyList(list):
    """
    This class inherits from list.

    Attributes:
    Methods:
        print_sorted - Prints list in ascending order
    """
    def print_sorted(self):
        """
        prints a list in ascending order.
        """
        print(sorted(self))
