import pytest

from algorithms.basic.bsearch import bsearch_iterative, bsearch_recursive


@pytest.mark.array
class TestBinarySearch:
    @pytest.mark.parametrize("i", [4, 0, 10])
    @pytest.mark.parametrize("func", [bsearch_iterative, bsearch_recursive])
    def test_bsearch_good(self, func, i):
        arr = [0, 2, 4, 6, 8, 10]
        assert func(arr, i) is True

    @pytest.mark.parametrize("i", [3, 1, 11])
    @pytest.mark.parametrize("func", [bsearch_iterative, bsearch_recursive])
    def test_bsearch_bad(self, func, i):
        arr = [0, 2, 4, 6, 8, 10]
        assert func(arr, i) is False
