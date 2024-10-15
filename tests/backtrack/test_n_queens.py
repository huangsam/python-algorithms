import pytest

from algorithms.backtrack.n_queens import n_queens


@pytest.mark.array
@pytest.mark.backtrack
@pytest.mark.parametrize("dim", range(4, 9))
def test_n_queens(dim: int):
    board = [[0] * dim for _ in range(dim)]
    assert n_queens(board, 0) is True
