#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return {k: (v*2) if a_dictionary else {} for k, v in a_dictionary.items()}
