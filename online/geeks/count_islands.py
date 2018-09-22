def count_islands(grid):
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                result += 1
                visit_island(i, j, grid)
    return result


# https://www.geeksforgeeks.org/find-number-of-islands/
def visit_island(i, j, grid):
    if i < 0 or j < 0:
        return
    elif i >= len(grid) or j >= len(grid[0]):
        return
    elif grid[i][j] == 0:
        return
    grid[i][j] = 0
    visit_island(i - 1, j, grid)
    visit_island(i + 1, j, grid)
    visit_island(i, j - 1, grid)
    visit_island(i, j + 1, grid)
    visit_island(i - 1, j - 1, grid)
    visit_island(i + 1, j + 1, grid)
    visit_island(i - 1, j + 1, grid)
    visit_island(i + 1, j - 1, grid)
