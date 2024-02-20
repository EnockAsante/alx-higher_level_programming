#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for i, (k, v) in enumerate(a_dictionary.items()):
        if k == key:
            k: value
            return a_dictionary
        else:
            a_dictionary[key] = value
    return a_dictionary
