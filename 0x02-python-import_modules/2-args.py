#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    counter = 0
    len_ = len(argv) - 1
    if len_ > 1 or len_ == 0:
        print("{:d} argument".format(len_), end="s:\n" if len_ > 1 else "s.\n")
    else:
        print("{:d} argument".format(len_), end=":\n")
    for i in argv:
        if counter > 0:
            print("{:d}: {}".format(counter, i))
        counter += 1
