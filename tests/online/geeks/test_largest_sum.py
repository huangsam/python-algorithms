import pytest

from online.geeks.largest_sum import (
    largest_sum_non_adjacent,
    largest_sum_adjacent,
)


class TestLargestSum(object):

    @pytest.mark.parametrize("given, expected", [
        ([], 0),
        ([1], 1),
        ([2, 1], 2),
        ([5, 1, 1, 5], 10),
        ([2, 4, 6, 2, 5], 13),
        ([3, 2, 7, 10], 13),
        ([3, 2, 5, 10, 7], 15),
        ([6, 0, 0, 92, 12], 98),
    ])
    def test_largest_sum_non_adjacent(self, given, expected):
        assert largest_sum_non_adjacent(given) == expected

    @pytest.mark.parametrize("given, expected", [
        ([], 0),
        ([-1], 0),
        ([-1, 2], 2),
        ([2, 6, -13, 9, 3, -3, 5, 6], 20),
    ])
    def test_largest_sum_adjacent(self, given, expected):
        assert largest_sum_adjacent(given) == expected
