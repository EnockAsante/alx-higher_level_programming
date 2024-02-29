#!/usr/bin/python3
def safe_print_list_integers(my_list = [], x = 0):
    counter = 0
    try:
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end = "")
            counter += 1
        return counter
    except (ValueError, IndexError, TypeError):
        pass
    finally:
        print()


my_list = [1, 2, 3, 4]
x = len(my_list) + 4
nb_print = safe_print_list_integers(my_list, x)
print("{:d}".format(nb_print))