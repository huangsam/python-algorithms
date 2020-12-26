import pytest

from algorithms.online.geeks.product_array import product_array


@pytest.mark.math
@pytest.mark.array
@pytest.mark.parametrize(
    "old, expected",
    [
        ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
        ([10, 3, 5, 6, 2], [180, 600, 360, 300, 900]),
        ([0, 5, 10, 20], [1000, 0, 0, 0]),
    ],
)
def test_product_array(old, expected):
    new_arr = product_array(old)
    for i, j in zip(new_arr, expected):
        assert i == j
