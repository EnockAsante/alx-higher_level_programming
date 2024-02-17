#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for elem in row:
                print("{}".format(elem), end=" ")
            print(end="\n")
