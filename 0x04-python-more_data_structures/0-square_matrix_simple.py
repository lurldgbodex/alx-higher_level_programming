#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_square = [[col ** 2 for col in row] for row in matrix]
    return matrix_square
