#!/usr/bin/python3
"""
mod add item
"""
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


new_list = load_from_json_file("add_item.json")
if not new_list:
    new_list = []
for idx, arg in enumerate(argv):
    if idx > 0:
        new_list.append(arg)
save_to_json_file(new_list, "add_item.json")
