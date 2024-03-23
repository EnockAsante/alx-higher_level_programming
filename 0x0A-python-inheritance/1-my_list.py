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
        if self:
            print(sorted(self))
