from basic.bsearch import (
    bsearch_recursive,
    bsearch_iterative,
)


class TestBinarySearch(object):

    def test_bsearch_recursive_good(self):
        arr = [0, 2, 4, 6, 8, 10]
        assert bsearch_recursive(arr, 4, 0, len(arr)) is True
        assert bsearch_recursive(arr, 0, 0, len(arr)) is True
        assert bsearch_recursive(arr, 10, 0, len(arr)) is True

    def test_bsearch_recursive_bad(self):
        arr = [0, 2, 4, 6, 8, 10]
        assert bsearch_recursive(arr, 3, 0, len(arr)) is False
        assert bsearch_recursive(arr, 1, 0, len(arr)) is False
        assert bsearch_recursive(arr, 11, 0, len(arr)) is False

    def test_bsearch_iterative_good(self):
        arr = [0, 2, 4, 6, 8, 10]
        assert bsearch_iterative(arr, 4) is True
        assert bsearch_iterative(arr, 0) is True
        assert bsearch_iterative(arr, 10) is True

    def test_bsearch_iterative_bad(self):
        arr = [0, 2, 4, 6, 8, 10]
        assert bsearch_iterative(arr, 3) is False
        assert bsearch_iterative(arr, 1) is False
        assert bsearch_iterative(arr, 11) is False
