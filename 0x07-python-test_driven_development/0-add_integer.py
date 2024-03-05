#!/usr/bin/python3
# Filename: 0-add-integer.py
def add_integer(a, b = 98):
    """add_integer - add two numbers
    :@param a=lo
    :@param b=ro
    :return result
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
