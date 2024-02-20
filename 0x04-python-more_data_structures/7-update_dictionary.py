#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for i, (k, v) in enumerate(a_dictionary.items()):
        if k == key:
            k: value
            return a_dictionary
        elif k != key and i == len(a_dictionary) - 1:
            a_dictionary[key] = value
    return a_dictionary
