#!/usr/bin/python3
"""
mod base
"""


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        return str(list_dictionaries)
