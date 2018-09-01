from basic.bsearch import bsearch_recursive


class TestBinarySearch(object):

    def test_bsearch_recursive_good(self):
        arr = [0, 2, 4, 6, 8, 10]
        result = bsearch_recursive(arr, 4, 0, len(arr))
        assert result is True
        result = bsearch_recursive(arr, 0, 0, len(arr))
        assert result is True
        result = bsearch_recursive(arr, 10, 0, len(arr))
        assert result is True

    def test_bsearch_recursive_bad(self):
        arr = [0, 2, 4, 6, 8, 10]
        result = bsearch_recursive(arr, 3, 0, len(arr))
        assert result is False
        result = bsearch_recursive(arr, 1, 0, len(arr))
        assert result is False
        result = bsearch_recursive(arr, 11, 0, len(arr))
        assert result is False
