#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        jout = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            jout += 1
        print()
        return jout
    except IndexError:
        print()
        return jout
