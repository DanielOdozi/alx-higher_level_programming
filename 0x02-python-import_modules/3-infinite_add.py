#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sum = 0
    sumlen = len(argv)
    for i in range(1, sumlen):
        sum += int(argv[i])
    print("{}".format(sum))
