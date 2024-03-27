#!/usr/bin/python3
"""
mod base
"""


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id = None):
        if id:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
