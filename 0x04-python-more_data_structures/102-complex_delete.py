#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_del = []
    for i, j in a_dictionary.items():
        if j == value:
            key_del.append(i)
    for i in key_del:
        del a_dictionary[i]
    return a_dictionary
