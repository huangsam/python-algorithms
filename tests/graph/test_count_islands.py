import pytest

from algorithms.graph.count_islands import count_islands


@pytest.mark.graph
@pytest.mark.parametrize(
    "grid, answer",
    [
        ([[1, 0, 1], [0, 0, 0], [1, 0, 1]], 4),
        ([[1, 0, 1], [1, 0, 1], [1, 0, 1]], 2),
        ([[1, 0, 1], [0, 1, 0], [1, 0, 1]], 1),
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
    ],
)
def test_count_islands(grid: list[list[int]], answer: int):
    assert count_islands(grid) == answer
