from copy import deepcopy


def rotateImage(a):
    a = deepcopy(a)
    a_len = len(a)
    # squares
    for x in range(a_len // 2):
        # elements
        for y in range(x, a_len - x - 1):
            north = a[x][y]
            # top <- left
            a[x][y] = a[a_len - y - 1][x]
            # left <- bottom
            a[a_len - y - 1][x] = a[a_len - x - 1][a_len - y - 1]
            # bottom <- right
            a[a_len - x - 1][a_len - y - 1] = a[y][a_len - x - 1]
            # right <- top
            a[y][a_len - x - 1] = north
    return a


def printImage(a):
    print("---")
    for i in range(len(a)):
        print("|".join(map(str, a[i])))
    print("---")
