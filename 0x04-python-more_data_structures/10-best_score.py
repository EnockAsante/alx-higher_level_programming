#!/usr/bin/python3
def best_score(a_dictionary):
    n = "None" if not a_dictionary else sorted(a_dictionary)[0]
    return n

a = {'e':700, 'w':"e", 'e':20}
print(best_score(a))
print(a)