import pytest

from basic.factorial import (
    factorial_recursive,
    factorial_stack,
)


class TestFactorial(object):

    @pytest.mark.parametrize('func', [
        factorial_recursive,
        factorial_stack,
    ])
    @pytest.mark.parametrize('i,o', [
        (0, 1),
        (1, 1),
        (4, 24),
        (5, 120),
    ])
    def test_factorial(self, func, i, o):
        assert func(i) == o
