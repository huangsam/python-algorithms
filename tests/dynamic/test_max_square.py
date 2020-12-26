import pytest

from algorithms.dynamic import max_square as maxsq


@pytest.mark.array
@pytest.mark.dynamic
@pytest.mark.parametrize("i", [1, 2, 3, 4])
def test_max_square_empty(i):
    m = [[0] * i for _ in range(i)]
    assert maxsq.max_square(m) == 0


@pytest.mark.array
@pytest.mark.dynamic
@pytest.mark.parametrize("i", [1, 2, 3, 4])
def test_max_square_full(i):
    m = [[1] * i for _ in range(i)]
    assert maxsq.max_square(m) == i


@pytest.mark.array
@pytest.mark.dynamic
def test_max_square_partial():
    m = [[0, 0, 0], [1, 1, 1], [1, 1, 1]]
    assert maxsq.max_square(m) == 2


@pytest.mark.array
@pytest.mark.dynamic
def test_max_square_one():
    m = [[0, 0, 0], [0, 0, 0], [1, 1, 1]]
    assert maxsq.max_square(m) == 1


@pytest.mark.array
@pytest.mark.dynamic
def test_max_square_none():
    m = [[0]]
    assert maxsq.max_square(m) == 0
