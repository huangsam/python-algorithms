import pytest

from algorithms.basic.multiply import multiply


@pytest.mark.math
@pytest.mark.parametrize("x,y", [(2, 0), (0, 2), (0, 0)])
def test_multiply_zero(x, y):
    assert multiply(x, y) == 0


@pytest.mark.math
def test_multiply_even():
    assert multiply(3, 6) == 18


@pytest.mark.math
def test_multiply_odd():
    assert multiply(6, 3) == 18


@pytest.mark.math
@pytest.mark.parametrize("x,y", [(-1, 1), (1, -1), (-1, -1)])
def test_multiply_neg(x, y):
    with pytest.raises(ValueError):
        multiply(x, y)
