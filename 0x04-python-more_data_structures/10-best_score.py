#!/usr/bin/python3
def best_score(a_dictionary):
    n = "None" if not a_dictionary else sorted(a_dictionary.items(),
                                               reverse=True)[0]
    return n

