#!/usr/bin/python3
"""
mod instance
"""


def is_kind_of_class(obj, a_class):
    """

    :param obj:
    :param a_class:
    :return:
    """
    if type(obj) is a_class:
        return True
    for sub in a_class.__subclasses__():
        if type(obj) is sub:
            return True
    return False
