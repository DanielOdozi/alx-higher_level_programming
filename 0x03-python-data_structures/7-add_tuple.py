#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    newtuple = ()
    for i in range(len(tuple_a)):
        newtuple += (tuple_a[i] + tuple_b[i],)
    return newtuple