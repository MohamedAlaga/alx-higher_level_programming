#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for item in matrix:
            for num in item:
                print("{}".format(num), end=" ")
            print("")
