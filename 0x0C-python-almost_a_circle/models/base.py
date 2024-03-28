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

    @classmethod
    def save_to_file(cls, list_objs):
        """

        :param list_objs:
        :return:
        """

        with open(cls.__name__ + ".json", "w", encoding="UTF8") as f:
            lst = []
            if list_objs:
                for obj in list_objs:
                    lst.append(obj.to_dictionary())
                return f.write(cls.to_json_string(lst))




