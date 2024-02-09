#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    counter = 0
    print("{:d} arguments".format(len(argv) - 1), end = ":\n" if len(argv) - 1 \
                                                                 >= 1 else
    ".\n")
    for i in argv:
        if counter > 0:
            print("{:d}: {}".format(counter, i))
        counter += 1
