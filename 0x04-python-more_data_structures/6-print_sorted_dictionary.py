#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    d = dict(sorted(a_dictionary.items()))
    for key, value in d.items():
        print("{}: {}".format(key, value))
