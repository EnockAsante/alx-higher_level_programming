#!/usr/bin/python3
"""
mod append file
"""


def append_write(filename="", text=""):
    """

    :param filename:
    :param text:
    :return:
    """
    with open(filename, "a", encoding="UFT8") as f:
        return f.write(text)
