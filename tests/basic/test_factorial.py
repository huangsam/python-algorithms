import pytest

from basic.factorial import (
    factorial_recursive,
    factorial_stack,
    factorial_dp_bottom,
    factorial_dp_top,
)


@pytest.mark.dynamic
class TestFactorial(object):
    @pytest.mark.parametrize(
        "func",
        [factorial_recursive, factorial_stack, factorial_dp_bottom, factorial_dp_top],
    )
    @pytest.mark.parametrize("i,o", [(0, 1), (1, 1), (2, 2), (3, 6), (4, 24), (5, 120)])
    def test_factorial(self, func, i, o):
        assert func(i) == o
