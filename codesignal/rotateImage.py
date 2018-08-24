#!/bin/bash


def printMatrix(a):
    print("---")
    a_len = len(a)
    for i in range(a_len):
        print(a[i])


def rotateImage(a):
    a_len = len(a)
    # squares
    for x in range(int(a_len/2)):
        # elements
        for y in range(x, a_len-x-1):
            north = a[x][y]
            # left -> top
            a[x][y] = a[a_len-1-y][x]
            # bottom -> left
            a[a_len-1-y][x] = a[a_len-1-x][a_len-1-y]
            # right -> bottom
            a[a_len-1-x][a_len-1-y] = a[y][a_len-1-x]
            # top -> right
            a[y][a_len-1-x] = north
    return a


three_a = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]

five_a = [
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5]
]

seven_a = [
    [1, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5, 5, 5],
    [6, 6, 6, 6, 6, 6, 6],
    [7, 7, 7, 7, 7, 7, 7]
]

# Provide input
a_in = seven_a

# Provide output
printMatrix(a_in)
result = rotateImage(a_in)
printMatrix(result)
