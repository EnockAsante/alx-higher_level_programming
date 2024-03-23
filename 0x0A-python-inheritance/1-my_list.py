#!/usr/bin/python3
"""
mod my list
"""


class MyList(list):
    """
    :mylist
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(list(self)))

    def __str__(self):
        """
        Returns the string representation of the list.
        """
        return str(self)
