import pytest

from algorithms.sorting import search_rotated as rotate


def rotate_(arr, n):
    x = arr[::-1]
    return x[:n][::-1] + x[n:][::-1]


def cycle_(n):
    arr = [_ for _ in range(1, n + 1)]
    return [rotate_(arr, i) for i in range(n)]


@pytest.mark.array
@pytest.mark.sorting
class TestSearchRotated:
    @pytest.mark.parametrize("a", cycle_(10))
    def test_search_rotated(self, a):
        for v in a:
            assert rotate.search_rotated(a, v) is True

    @pytest.mark.parametrize("a", cycle_(10))
    def test_search_min(self, a):
        assert rotate.search_min(a) == 1
