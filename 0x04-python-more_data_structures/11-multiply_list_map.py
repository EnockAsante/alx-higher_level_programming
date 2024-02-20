#!/usr/bin/python3
def multiply_list_map(my_list = [], number = 0):
    return {k: (v * number) if my_list else {} for k, v in my_list.items()}
