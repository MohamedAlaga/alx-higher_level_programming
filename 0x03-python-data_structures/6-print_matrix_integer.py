#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        lenth = 1
        for j in i:
            if lenth == len(i):
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
            lenth = lenth + 1
        print()
