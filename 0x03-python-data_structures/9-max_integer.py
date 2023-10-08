#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    new_list = my_list[0]
    for i in my_list:
        if i > new_list:
            new_list = i
            return new_list
