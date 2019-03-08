import pytest

from online.geeks.n_queens import n_queens


@pytest.mark.array
@pytest.mark.backtrack
class TestNQueens(object):
    @pytest.mark.parametrize("dim", range(4, 9))
    def test_n_queens(self, dim):
        board = [[0] * dim for i in range(dim)]
        valid = n_queens(board, 0)
        assert valid is True
