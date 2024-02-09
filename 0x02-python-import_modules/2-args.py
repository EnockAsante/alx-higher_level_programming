from sys import argv
counter = 0
for i in argv:
    if counter < len(argv):
        print("{:d}: {}".format(counter, argv[:counter]))
