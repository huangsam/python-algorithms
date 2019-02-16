import pytest

from basic.multiply import multiply


class TestMultiply(object):

    def test_multiply_zero(self):
        assert multiply(0, 2) == 0
        assert multiply(2, 0) == 0

    def test_multiply_even(self):
        assert multiply(2, 4) == 8
        assert multiply(3, 6) == 18
        assert multiply(6, 3) == 18

    def test_multiply_odd(self):
        assert multiply(2, 5) == 10

    def test_multiply_neg(self):
        with pytest.raises(ValueError):
            multiply(-1, 5)
        with pytest.raises(ValueError):
            multiply(5, -1)
        with pytest.raises(ValueError):
            multiply(-1, -1)
