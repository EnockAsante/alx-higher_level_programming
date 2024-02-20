#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    d = {k: value if k == key else v for k, v in a_dictionary.items()}
    for i, (k, v) in enumerate(d.items()):
        if k != key and i == len(d) - 1:
            d[key] = value
            return d
    return d

