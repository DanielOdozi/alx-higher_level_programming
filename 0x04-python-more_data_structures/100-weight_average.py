#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weight_sum = 0
    total_sum = 0
    for num, weight in my_list:
        weight_sum += num * weight
        total_sum += weight
    return weight_sum/total_sum
