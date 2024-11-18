# https://www.geeksforgeeks.org/find-number-of-islands/
def count_islands(grid: list[list[int]]):
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                result += 1
                _visit_island(i, j, grid)
    return result


def _visit_island(i: int, j: int, grid: list[list[int]]):
    if i < 0 or j < 0:
        return
    elif i >= len(grid) or j >= len(grid[0]):
        return
    elif grid[i][j] == 0:
        return
    grid[i][j] = 0
    _visit_island(i - 1, j, grid)
    _visit_island(i + 1, j, grid)
    _visit_island(i, j - 1, grid)
    _visit_island(i, j + 1, grid)
    _visit_island(i - 1, j - 1, grid)
    _visit_island(i + 1, j + 1, grid)
    _visit_island(i - 1, j + 1, grid)
    _visit_island(i + 1, j - 1, grid)
