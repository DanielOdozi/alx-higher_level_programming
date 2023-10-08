#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    new_list = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > new_list:
            new_list = my_list[i]
            return new_list
