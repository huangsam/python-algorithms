import pytest

from algorithms.sorting import search_rotated as rotate


def _rotate(arr, n):
    x = arr[::-1]
    return x[:n][::-1] + x[n:][::-1]


def _cycle(n, start=1):
    arr = [start + 3 * i for i in range(n)]
    return [_rotate(arr, i) for i in range(n)]


@pytest.mark.array
@pytest.mark.sorting
@pytest.mark.parametrize("a", _cycle(5))
def test_search_one(a):
    for v in a:
        assert rotate.search_one(a, v) is True


@pytest.mark.array
@pytest.mark.sorting
@pytest.mark.parametrize("a", _cycle(5))
def test_search_min(a):
    assert rotate.search_min(a) == min(a)


@pytest.mark.array
@pytest.mark.sorting
def test_search_min_dupe():
    a = [3, 3, 3, 5, 5, 7, 9, 9, 9, 1, 1, 2, 2, 2]
    assert rotate.search_min(a) == min(a)
