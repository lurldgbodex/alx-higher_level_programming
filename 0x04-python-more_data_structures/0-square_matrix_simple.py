#!/usr/python3
def square_matrix_simple(matrix=[]):
    matrix_square = [[i ** 2 for i in row] for row in matrix]
    return matrix_square
