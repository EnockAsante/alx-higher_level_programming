#!/usr/bin/python3
"""
read_file mod
"""


def read_file(filename = ""):
    """

    :param filename:
    :return:
    """
    with open(filename, 'r', encoding = "UTF8") as f:
        for line in f:
            print("{}".format(line), end = "")
