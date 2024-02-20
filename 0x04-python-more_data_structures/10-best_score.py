#!/usr/bin/python3
def best_score(a_dictionary):
    n = "None" if not a_dictionary else sorted(a_dictionary, reverse = True)[0]
    return n


a = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
print(best_score(a))
print(a)
