#!/usr/bin/python3
"""
mod class to json
"""


class Student:
    def __init__(self, fname, lname, age):
        self.first_name = fname
        self.last_name = lname
        self.age = age

    def to_json(self, attrs = None):
        dic = vars(self)
        new_dic = {}
        if type(attrs) is list:
            for item in attrs:
                for k, v in dic.items():
                    if item == k:
                        new_dic[k] = v
            return new_dic
        else:
            return dic