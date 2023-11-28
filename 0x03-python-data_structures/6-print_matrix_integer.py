#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for item in matrix:
            for num in item:
                if num == matrix[-1]:
                    print("{:d}".format(num), end="")
                else:
                    print("{:d}".format(num), end=" ")
            print()
