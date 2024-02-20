#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    del dict(a_dictionary)[key]
    return {a_dictionary}
