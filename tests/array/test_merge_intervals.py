import pytest

from algorithms.array.merge_intervals import merge_intervals


@pytest.mark.array
@pytest.mark.parametrize(
    "intervals, expected",
    [([[1, 3], [2, 6], [8, 10], [15, 18]], 3), ([[3, 6], [4, 5]], 1)],
)
def test_merge_intervals(intervals: list[list[int]], expected: int):
    result = merge_intervals(intervals)
    assert len(result) == expected
