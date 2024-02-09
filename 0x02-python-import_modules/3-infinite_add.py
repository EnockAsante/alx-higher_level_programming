#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    counter = 0
    sum = 0
    for i in argv:
        if counter > 0:
            sum += int(i)
        counter += 1
    print("{:d}".format(sum))
