import pytest

from algorithms.dynamic import subset_sum as sub


@pytest.mark.dynamic
class TestSubsetSum:
    @pytest.mark.parametrize("n", [1, 6, 13])
    @pytest.mark.parametrize("func", [sub.subset_sum_rec, sub.subset_sum_dp])
    def test_subset_sum_good(self, func, n):
        nums = {3, 2, 7, 1, 99}
        assert func(nums, n)

    @pytest.mark.parametrize("n", [14, 15, 30])
    @pytest.mark.parametrize("func", [sub.subset_sum_rec, sub.subset_sum_dp])
    def test_subset_sum_bad(self, func, n):
        nums = {3, 2, 7, 1, 99}
        assert not func(nums, n)
