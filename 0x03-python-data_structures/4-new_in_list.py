#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy = my_list.copy()
    if 0 <= idx < len(my_list):
        cpy[idx] = element
        return cpy
    else:
        return my_list
