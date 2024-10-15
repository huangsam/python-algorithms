import pytest

from algorithms.dynamic.lis import lis


@pytest.mark.array
@pytest.mark.dynamic
@pytest.mark.parametrize("n", [1, 5, 100])
def test_lis_always(n: int):
    assert lis(list(range(n))) == n


@pytest.mark.array
@pytest.mark.dynamic
@pytest.mark.parametrize("n", [1, 5, 100])
def test_lis_never(n: int):
    assert lis(list(range(n - 1, -1, -1))) == 1


@pytest.mark.array
@pytest.mark.dynamic
def test_lis_mixed_small():
    assert lis([1, 12, 7]) == 2


@pytest.mark.array
@pytest.mark.dynamic
def test_lis_mixed_big():
    assert lis([1, 12, 7, 0, 23, 11, 52, 31, 61, 69, 70, 2]) == 7


@pytest.mark.array
@pytest.mark.dynamic
def test_lis_empty():
    assert lis([]) == 0
