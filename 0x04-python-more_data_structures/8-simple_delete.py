#!/usr/bin/python3
def simple_delete(a_dictionary, key = ""):
    oc_counts = 0
    for k, v in a_dictionary.items():
        if k == key:
            oc_counts += 1
    while oc_counts > 0:
        del a_dictionary[key]
        oc_counts -= 1
    return a_dictionary
