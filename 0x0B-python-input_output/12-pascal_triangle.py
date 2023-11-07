#!/usr/bin/python3
"""function that returns list of integers representing the Pascal’s triangle"""


def pascal_triangle(n):
    """returns list of integers representing the Pascal’s triangle.

    Args:
        n (int): The value for pascal's triangle.
    """
    new_list = []
    if n <= 0:
        return new_list

    if not isinstance(n, int):
        raise TypeError("Value must be integer")

    for i in range(n):
        if i == 0:
            new_list.append([1])
        else:
            prev_row = new_list[i - 1]
            new_row = [1]
            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j])
            new_row.append(1)
            new_list.append(new_row)

    return new_list
