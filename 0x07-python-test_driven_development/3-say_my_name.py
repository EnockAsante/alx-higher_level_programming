#!/usr/bin/python3

"""
say my name
"""


def say_my_name(first_name, last_name = ""):
    """
    :param first_name:
    :param last_name:
    :return:
    """
    for j, i in enumerate([first_name, last_name]):
        if i or type(i) is not str:
            raise (TypeError("first_name must be a string" if j == 0 else
                             "last_name must be a string"))
    print("My name is {} {}".format(first_name, last_name))

