#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for k, v in dict(a_dictionary.items()):
        if k == key:
            k: value
            return a_dictionary
    a_dictionary[key] = value
    return a_dictionary
