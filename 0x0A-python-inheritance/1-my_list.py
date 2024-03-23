#!/usr/bin/python3
"""
mod my list
"""


class MyList(list):
    """
    :mylist
    """
    def print_sorted(self):
        print(sorted(list(self)))
