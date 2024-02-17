def add_tuple(tuple_a = (), tuple_b = ()):
    tuple_res = ()
    if tuple_a and tuple_b:
        if 2 > len(tuple_a) < len(tuple_b):
            tuple_a += (0,)
        elif 2 > len(tuple_b) < len(tuple_a):
            tuple_b += (0,)
    for i, elem in enumerate(tuple_a):
        if i < 2:
            tuple_res += (tuple_a[i] + tuple_b[i],)
    return tuple_res
