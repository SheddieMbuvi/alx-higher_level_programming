#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        transpose = []
        for item in row:
            item = item * item
            transpose.append(item)
        new_matrix.append(transpose)
    return new_matrix
