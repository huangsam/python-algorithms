# https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
def n_queens(board: list[list[int]], col: int):
    if col >= len(board):
        return True

    # Try all rows in current column
    for row in range(len(board)):
        if _is_safe(board, row, col) is True:
            board[row][col] = 1
            if n_queens(board, col + 1) is True:
                return True
            board[row][col] = 0
    return False


def _is_safe(board: list[list[int]], row: int, col: int):
    for i in range(len(board)):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1), strict=False):
        if board[i][j] == 1:
            return False

    # Check lower diagonal
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1), strict=False):
        if board[i][j] == 1:
            return False

    return True
