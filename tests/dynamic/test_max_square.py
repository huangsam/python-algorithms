import pytest

from algorithms.dynamic.max_square import max_square


@pytest.mark.array
@pytest.mark.dynamic
@pytest.mark.parametrize("i", [1, 2, 3, 4])
def test_max_square_empty(i: int):
    assert max_square([[0] * i for _ in range(i)]) == 0


@pytest.mark.array
@pytest.mark.dynamic
@pytest.mark.parametrize("i", [1, 2, 3, 4])
def test_max_square_full(i: int):
    assert max_square([[1] * i for _ in range(i)]) == i


@pytest.mark.array
@pytest.mark.dynamic
def test_max_square_partial():
    assert max_square([[0, 0, 0], [1, 1, 1], [1, 1, 1]]) == 2


@pytest.mark.array
@pytest.mark.dynamic
def test_max_square_one():
    assert max_square([[0, 0, 0], [0, 0, 0], [1, 1, 1]]) == 1


@pytest.mark.array
@pytest.mark.dynamic
def test_max_square_none():
    assert max_square([[0]]) == 0
