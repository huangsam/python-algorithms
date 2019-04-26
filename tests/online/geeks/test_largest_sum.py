import pytest

from algorithms.online.geeks.largest_sum import (
    largest_sum_non_adjacent,
    largest_sum_adjacent,
)


@pytest.mark.array
class TestLargestSum:
    @pytest.mark.parametrize(
        "given, expected",
        [
            ([], 0),
            ([1], 1),
            ([2, 1], 2),
            ([5, 1, 1, 5], 10),
            ([2, 4, 6, 2, 5], 13),
            ([3, 2, 7, 10], 13),
            ([3, 2, 5, 10, 7], 15),
            ([6, 0, 0, 92, 12], 98),
            ([-1, 0, -3, 5, 8], 8),
        ],
    )
    def test_largest_sum_non_adjacent(self, given, expected):
        assert largest_sum_non_adjacent(given) == expected

    @pytest.mark.parametrize(
        "given, expected",
        [([], 0), ([1], 1), ([-1], 0), ([-1, 2], 2), ([2, 6, -13, 9, 3, -3, 5, 6], 20)],
    )
    def test_largest_sum_adjacent(self, given, expected):
        assert largest_sum_adjacent(given) == expected
