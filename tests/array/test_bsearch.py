import pytest

from algorithms.array.binary_search import (
    binary_search_iterative,
    binary_search_recursive,
)


@pytest.mark.array
@pytest.mark.parametrize("func", [binary_search_iterative, binary_search_recursive])
def test_bsearch_good(func):
    arr = [0, 2, 4, 6, 8, 10]
    for ix, v in enumerate(arr):
        assert func(arr, v) == ix


@pytest.mark.array
@pytest.mark.parametrize("func", [binary_search_iterative, binary_search_recursive])
def test_bsearch_bad(func):
    arr = [0, 2, 4, 6, 8, 10]
    for v in arr:
        assert func(arr, v - 1) == -1
