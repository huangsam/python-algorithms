import pytest

from algorithms.basic import bsearch


@pytest.mark.array
class TestBinarySearch:
    @pytest.mark.parametrize(
        "func", [bsearch.bsearch_iterative, bsearch.bsearch_recursive]
    )
    def test_bsearch_good(self, func):
        arr = [0, 2, 4, 6, 8, 10]
        for v in arr:
            assert func(arr, v) is True

    @pytest.mark.parametrize(
        "func", [bsearch.bsearch_iterative, bsearch.bsearch_recursive]
    )
    def test_bsearch_bad(self, func):
        arr = [0, 2, 4, 6, 8, 10]
        for v in arr:
            assert func(arr, v - 1) is False
