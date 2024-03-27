#!/usr/bin/python3
"""
mod base
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """

        :return:
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        with open("{}.json".format(cls.__name__), 'a', encoding="UTF8") as f:
            if list_objs:
                f.write(cls.to_json_string(list_objs))
            else:
                f.write("")
