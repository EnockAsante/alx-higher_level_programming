#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """
    class of Square
    """
    def __init__(self, size=0):
        """constructor for initialising the instance variable
        :@size = size(private) to use"""
        try:
            if type(size) is int:
                if size < 0:
                    raise ValueError
                else:
                    self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
