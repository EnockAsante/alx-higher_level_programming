#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for i, elem in enumerate(row):
                print("{:d}".format(elem), end=" " if i < len(row)-1 else "\n")
    else:
        print("\n", end="")
