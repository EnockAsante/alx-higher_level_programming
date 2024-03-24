#!/usr/bin/python3
"""
mod write file
"""


def write_file(filename="", text=""):
    """

    :param filename:
    :param text:
    :return:
    """
    with open(filename, "w", encoding="UTF8") as f:
        f.write(text)
