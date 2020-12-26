import pytest

from algorithms.array.bsearch import bsearch_iterative, bsearch_recursive


@pytest.mark.array
@pytest.mark.parametrize("func", [bsearch_iterative, bsearch_recursive])
def test_bsearch_good(func):
    arr = [0, 2, 4, 6, 8, 10]
    for ix, v in enumerate(arr):
        assert func(arr, v) == ix


@pytest.mark.array
@pytest.mark.parametrize("func", [bsearch_iterative, bsearch_recursive])
def test_bsearch_bad(func):
    arr = [0, 2, 4, 6, 8, 10]
    for v in arr:
        assert func(arr, v - 1) == -1
