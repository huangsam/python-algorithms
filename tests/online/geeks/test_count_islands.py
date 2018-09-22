import pytest

from online.geeks.count_islands import count_islands


class TestCountIslands(object):

    @pytest.mark.parametrize("grid, answer", [
        ([
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1],
        ], 5),
    ])
    def test_count_islands(self, grid, answer):
        assert count_islands(grid) == answer
