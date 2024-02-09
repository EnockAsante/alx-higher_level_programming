#!/usr/bin/python3
from sys import argv

counter = 1
for i in argv:
    print("{:d}: {}".format(counter, i))
    counter += 1
