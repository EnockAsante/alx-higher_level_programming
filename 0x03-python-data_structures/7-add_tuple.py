#!/usr/bin/python3
def add_tuple(tuple_a = (), tuple_b = ()):
    tuple_res = ()
    while len(tuple_a) < 2:
        tuple_a += (0,)
    while len(tuple_b) < 2:
        tuple_b += (0,)
    for i, elem in enumerate(tuple_a):
        if i < 2:
            tuple_res += (tuple_a[i] + tuple_b[i],)
    return tuple_res
