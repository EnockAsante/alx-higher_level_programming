#!/usr/bin/python3
def best_score(a_dictionary):
    l_i = len(a_dictionary) - 1
    n = "None" if not a_dictionary else sorted(a_dictionary)[l_i]
    return n
