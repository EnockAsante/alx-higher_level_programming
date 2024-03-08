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
    for i in [first_name, last_name]:
        if i == "None" or type(i) is not str:
            raise TypeError("first_name must be a string or last_name must "
                            "be a string")
    print("My name is {}".format(first_name), end = ' ' if last_name else '')
    if last_name:
        print("{}".format(last_name))


