import pytest

from basic.fibonacci import (
    fibonacci_recursive,
    fibonacci_iterative,
    fibonacci_stack,
    fibonacci_dp_bottom,
    fibonacci_dp_top,
)


@pytest.mark.dynamic
class TestFibonacci(object):
    @pytest.mark.parametrize(
        "func",
        [
            fibonacci_iterative,
            fibonacci_recursive,
            fibonacci_stack,
            fibonacci_dp_bottom,
            fibonacci_dp_top,
        ],
    )
    @pytest.mark.parametrize(
        "i,o", [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8)]
    )
    def test_fibonacci(self, func, i, o):
        assert func(i) == o
