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
