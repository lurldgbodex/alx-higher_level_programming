#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in matrix:
            print("{}".format(col), end=" " if col != row[-1] else "")
