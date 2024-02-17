#!/usr/bin/python3
def element_at(my_list, idx):
    if 0 < idx < len(my_list):
        print("Element at index {:d} is {:d}".format(idx, my_list[idx]))
    else:
        print("None")


a = [1, 2, 3, 4, 5]
element_at(a, 2)
