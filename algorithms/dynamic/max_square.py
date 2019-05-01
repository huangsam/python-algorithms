# https://algorithms.tutorialhorizon.com//dynamic-programming-maximum-size-square-sub-matrix-with-all-1s/
def max_square(matrix):
    m, n = len(matrix), len(matrix[0])
    size = [[0] * n for _ in range(m)]
    for i in range(m):
        size[i][0] = matrix[i][0]
    for i in range(n):
        size[0][i] = matrix[0][i]
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                continue
            up = size[i - 1][j]
            left = size[i][j - 1]
            diag = size[i - 1][j - 1]
            size[i][j] = min(up, left, diag) + 1
    return size[m - 1][n - 1]
