#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        my_div = a / b
    except ZeroDivisionError:
        my_div = None
    finally:
        print("Inside result: {}".format(my_div))
    return my_div
