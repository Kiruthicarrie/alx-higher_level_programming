#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    if len(argv) == 1:
        print("{} arguments.".format(len(argv) - 1))
    elif len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
    else:
        print("{} arguments:".format(len(argv) - 1))

    for n in range(len(argv)):
        if n != 0:
            print("{}: {}".format(n, argv[n]))
