#!/usr/bin/python3
"""
copy list
"""
def copy_list(l):
    """
    creates list copy
    """
    if l:
        a = l[:]
        return a
    return None
