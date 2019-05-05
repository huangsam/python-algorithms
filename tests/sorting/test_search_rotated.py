import pytest

from algorithms.sorting import search_rotated as rotate


def rotate_(arr, n):
    x = arr[::-1]
    return x[:n][::-1] + x[n:][::-1]


def cycle_(n, start=1):
    arr = [start + 3 * i for i in range(n)]
    return [rotate_(arr, i) for i in range(n)]


@pytest.mark.array
@pytest.mark.sorting
class TestSearchRotated:
    @pytest.mark.parametrize("a", cycle_(5))
    def test_search_one(self, a):
        for v in a:
            assert rotate.search_one(a, v) is True

    @pytest.mark.parametrize("a", cycle_(5))
    def test_search_min(self, a):
        assert rotate.search_min(a) == min(a)

    def test_search_min_dupe(self):
        a = [3, 3, 3, 5, 5, 7, 9, 9, 9, 1, 1, 2, 2, 2]
        assert rotate.search_min(a) == min(a)
