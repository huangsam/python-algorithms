import pytest

from algorithms.dynamic.lis import lis


@pytest.mark.array
@pytest.mark.dynamic
@pytest.mark.parametrize("n", [1, 5, 100])
def test_lis_always(n):
    a = [_ for _ in range(n)]
    assert lis(a) == n


@pytest.mark.array
@pytest.mark.dynamic
@pytest.mark.parametrize("n", [1, 5, 100])
def test_lis_never(n):
    a = [_ for _ in range(n - 1, -1, -1)]
    assert lis(a) == 1


@pytest.mark.array
@pytest.mark.dynamic
def test_lis_mixed_small():
    a = [1, 12, 7]
    assert lis(a) == 2


@pytest.mark.array
@pytest.mark.dynamic
def test_lis_mixed_big():
    a = [1, 12, 7, 0, 23, 11, 52, 31, 61, 69, 70, 2]
    assert lis(a) == 7


@pytest.mark.array
@pytest.mark.dynamic
def test_lis_empty():
    a = []
    assert lis(a) == 0
