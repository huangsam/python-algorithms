def sudoku2(grid):
    for i in range(9):
        if rowValid(grid, i) is False:
            return False
        if columnValid(grid, i) is False:
            return False
    for i in range(3):
        for j in range(3):
            if gridValid(grid, i, j) is False:
                return False
    return True


def rowValid(grid, row):
    seen = set()
    i = 0
    for i in range(9):
        val = grid[row][i]
        if val in seen:
            return False
        if val != ".":
            seen.add(val)
    return True


def columnValid(grid, column):
    seen = set()
    i = 0
    for i in range(9):
        val = grid[i][column]
        if val in seen:
            return False
        if val != ".":
            seen.add(val)
    return True


def gridValid(grid, row, col):
    seen = set()
    for i in range(3 * row, 3 * (row + 1)):
        for j in range(3 * col, 3 * (col + 1)):
            val = grid[i][j]
            if val in seen and val != ".":
                return False
            if val != ".":
                seen.add(val)
    return True
