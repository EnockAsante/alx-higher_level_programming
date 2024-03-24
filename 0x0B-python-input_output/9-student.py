#!/usr/bin/python3
"""
mod class to json
"""


class Student:
    def __init__(self, fname, lname, age):
        self.first_name = fname
        self.last_name = lname
        self.age = age

    def to_json(self):
        return vars(self)
