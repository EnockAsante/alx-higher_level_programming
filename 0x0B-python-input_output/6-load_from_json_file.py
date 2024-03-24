#!/usr/bin/python3
"""
load JSON file
"""
import json


def load_from_json_file(filename):
    """

    :param filename:
    :return:
    """
    with open(filename, "r", encoding="UTF8") as f:
        return json.loads(f.read())
