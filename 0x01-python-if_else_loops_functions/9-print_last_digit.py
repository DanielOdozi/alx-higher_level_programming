#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        num = number % -10
    else:
        num = number % 10
    print("{}".format(abs(num)), end="")
    return ("{}".format(abs(num)))
