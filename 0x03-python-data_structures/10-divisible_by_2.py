#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_list = []
    if my_list:
        for i, elem in enumerate(my_list):
            if elem % 2 == 0:
                bool_list.append(1)
            else:
                bool_list.append(0)
        return bool_list
    else:
        return "None"
