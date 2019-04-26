import pytest

from algorithms.basic.multiply import multiply


class TestMultiply:
    @pytest.mark.parametrize("x,y", [(2, 0), (0, 2), (0, 0)])
    def test_multiply_zero(self, x, y):
        assert multiply(x, y) == 0

    def test_multiply_even(self):
        assert multiply(3, 6) == 18

    def test_multiply_odd(self):
        assert multiply(6, 3) == 18

    @pytest.mark.parametrize("x,y", [(-1, 1), (1, -1), (-1, -1)])
    def test_multiply_neg(self, x, y):
        with pytest.raises(ValueError):
            multiply(x, y)
