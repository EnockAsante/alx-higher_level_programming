#!/usr/bin/python3
"""
lookup mod
"""


def lookup(obj):
    """
    :param obj:
    :return:
    """
    return vars(obj) if obj else None
