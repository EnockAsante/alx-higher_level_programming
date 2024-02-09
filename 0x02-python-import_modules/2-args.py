#!/usr/bin/python3
from sys import argv

counter = 0
print("{:d} arguments :".format(len(argv) - 1))
for i in argv:
    if counter > 0:
        print("{:d}: {}".format(counter, i))
    counter += 1
