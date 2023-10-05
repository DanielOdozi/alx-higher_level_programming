#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    length = len(argv) - 1
    if length < 1:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
    else:
        print("{} arguments:".format(length))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
