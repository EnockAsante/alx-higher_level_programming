#!/usr/bin/python3
"""
save to  JSON file
"""
import json


def save_to_json_file(my_obj, filename):
    """

    :param my_obj:
    :param filename:
    :return:
    """
    with open(filename, "w", encoding="UTF8") as f:
        return f.write(json.dumps(my_obj))
