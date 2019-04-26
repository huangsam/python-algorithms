import pytest

from algorithms.online.geeks.count_islands import count_islands


@pytest.mark.graph
class TestCountIslands:
    @pytest.mark.parametrize(
        "grid, answer",
        [
            ([[1, 0, 1], [0, 0, 0], [1, 0, 1]], 4),
            ([[1, 0, 1], [1, 0, 1], [1, 0, 1]], 2),
            ([[1, 0, 1], [0, 1, 0], [1, 0, 1]], 1),
            ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
        ],
    )
    def test_count_islands(self, grid, answer):
        assert count_islands(grid) == answer
