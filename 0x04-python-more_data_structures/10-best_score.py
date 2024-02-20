#!/usr/bin/python3
def best_score(a_dictionary):
    n = "None" if not a_dictionary else sorted(a_dictionary.keys(),
                                               reverse=1)[0]
    return n

a = {'a':700, 'c':"e", 'e':20}
print(best_score(a))
print(a)