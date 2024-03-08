#!/usr/bin/python3

"""
print_square
"""


def print_square(size):
    """

    :param size:
    :return:
    """
    i = 0
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float):
        if size < 0:
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        str = "#" * (size ** 2)
        for j in (str):
            if i == size:
                print()
                i = 0
            print("{}".format(j), end ="")
            i += 1
        if str:
            print()
print_square(0)