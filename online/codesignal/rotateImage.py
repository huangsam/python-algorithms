from copy import deepcopy


def rotateImage(a):
    a = deepcopy(a)
    a_len = len(a)
    # squares
    for x in range(a_len//2):
        # elements
        for y in range(x, a_len-x-1):
            north = a[x][y]
            # top <- left
            a[x][y] = a[a_len-1-y][x]
            # left <- bottom
            a[a_len-1-y][x] = a[a_len-1-x][a_len-1-y]
            # bottom <- right
            a[a_len-1-x][a_len-1-y] = a[y][a_len-1-x]
            # right <- top
            a[y][a_len-1-x] = north
    return a
