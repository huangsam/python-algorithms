import pytest

from algorithms.array.binary_search import binary_search_iterative, binary_search_recursive


@pytest.mark.array
@pytest.mark.parametrize("func", [binary_search_iterative, binary_search_recursive])
def test_binary_search_get_match(func):
    arr = [0, 2, 4, 6, 8, 10]
    for ix, v in enumerate(arr):
        assert func(arr, v) == ix


@pytest.mark.array
@pytest.mark.parametrize("func", [binary_search_iterative, binary_search_recursive])
def test_binary_search_get_missing(func):
    arr = [0, 2, 4, 6, 8, 10]
    for v in arr:
        assert func(arr, v - 1) == -1
