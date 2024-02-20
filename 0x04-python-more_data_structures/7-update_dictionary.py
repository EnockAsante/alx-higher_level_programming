#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary = {k: value if k == key else v for k, v in a_dictionary.items()}
    for k, v in a_dictionary.items():
        if k != key:
            a_dictionary[key] = value
            return a_dictionary
    return a_dictionary
