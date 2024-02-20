#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary = {k: value if k == key else v for k, v in a_dictionary.items()}
    for i, (k, v) in enumerate(a_dictionary.items()):
        if k != key and i == len(a_dictionary) - 1:
            a_dictionary[key] = value
            return a_dictionary
    return a_dictionary
