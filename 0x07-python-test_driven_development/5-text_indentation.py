#!/usr/bin/python3

"""
text_indentation
"""


def text_indentation(text):
    j = 0
    """

    :param text:
    :return:
    """
    buffer = ""
    if text and type(text) is str:
        while j < len(text):
            buffer += text[j]
            if text[j] in '.?:':
                buffer += '\n\n'
                while j + 1 < len(text) and text[j + 1] == ' ':
                    j += 1
            j += 1
        print("{}".format(buffer), end='')
    else:
        raise TypeError("text must be a string")