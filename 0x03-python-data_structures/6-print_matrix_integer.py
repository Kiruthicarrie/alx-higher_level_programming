#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    n = 0
    m = 0
    for i in matrix:
        m = 0
        for j in i:
            if m < len(i)-1:
                print("{:d}".format(matrix[n][m]), end=" ")
            else:
                print("{:d}".format(matrix[n][m]), end="")
            m += 1
        print()
        n += 1
