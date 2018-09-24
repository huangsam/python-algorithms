import pytest

from online.geeks.largest_sum import largest_sum_non_adjacent


class TestLargestSum(object):

    @pytest.mark.parametrize("given, expected", [
        ([], 0),
        ([1], 1),
        ([2, 1], 2),
        ([5, 1, 1, 5], 10),
        ([2, 4, 6, 2, 5], 13),
        ([3, 2, 7, 10], 13),
        ([3, 2, 5, 10, 7], 15),
    ])
    def test_largest_sum(self, given, expected):
        assert largest_sum_non_adjacent(given) is expected
