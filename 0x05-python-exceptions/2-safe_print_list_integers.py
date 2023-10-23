#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        jout = 0
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                jout += 1
        print()
        return jout
    except ValueError:
        print()
        return jout
