import pytest

from algorithms.dynamic import subset_sum as sub


@pytest.mark.math
@pytest.mark.array
@pytest.mark.dynamic
@pytest.mark.parametrize("n", [1, 6, 13])
@pytest.mark.parametrize("func", [sub.subset_sum_rec, sub.subset_sum_dp])
def test_subset_sum_good(func, n):
    nums = {3, 2, 7, 1, 99}
    assert func(nums, n)


@pytest.mark.math
@pytest.mark.array
@pytest.mark.dynamic
@pytest.mark.parametrize("n", [14, 15, 30])
@pytest.mark.parametrize("func", [sub.subset_sum_rec, sub.subset_sum_dp])
def test_subset_sum_bad(func, n):
    nums = {3, 2, 7, 1, 99}
    assert not func(nums, n)
