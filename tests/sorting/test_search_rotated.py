import pytest

from algorithms.sorting import search_rotated as rotate


def rotate_(arr, n):
    x = arr[::-1]
    return x[:n][::-1] + x[n:][::-1]


class TestSearchRotated:
    @pytest.mark.parametrize("a", [rotate_([1, 2, 3, 4], i) for i in range(4)])
    def test_search_rotated(self, a):
        for v in a:
            assert rotate.search_rotated(a, v) is True
