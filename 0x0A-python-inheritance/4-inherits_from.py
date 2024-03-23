#!/usr/bin/python3
"""
mod instance
"""


def inherits_from(obj, a_class):
    """

    :param obj:
    :param a_class:
    :return:
    """
    for sub in a_class.__subclasses__():
        if isinstance(obj, sub):
            return True
    return False
