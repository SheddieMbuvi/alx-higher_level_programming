#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        row.append(list(map(lambda row: row**2, row)))
    return (new_matrix)
