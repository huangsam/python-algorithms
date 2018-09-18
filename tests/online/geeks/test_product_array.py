import pytest

from online.geeks.product_array import product_array


class TestProductArray(object):

    @pytest.mark.parametrize('old, expected', [
        ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
        ([10, 3, 5, 6, 2], [180, 600, 360, 300, 900]),
    ])
    def test_product_array(self, old, expected):
        new_arr = product_array(old)
        for i, j in zip(new_arr, expected):
            assert i == j