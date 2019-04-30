import pytest

from algorithms.dynamic import subset_sum as sub


@pytest.mark.dynamic
class TestSubsetSum:
    @pytest.mark.parametrize(
        "n, expected", [(1, True), (6, True), (13, True), (14, False)]
    )
    def test_rod_cutting_equal(self, n, expected):
        nums = {3, 2, 7, 1, 99}
        assert sub.subset_sum_rec(nums, n) is expected
