#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = [[y ** 2 for y in x]for x in matrix]
    print("{}".format(squares))