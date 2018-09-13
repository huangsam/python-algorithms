import pytest

from basic.fibonacci import (
    fibonacci_recursive,
    fibonacci_iterative,
    fibonacci_stack,
    fibonacci_dp_bottom,
)


class TestFibonacci(object):

    @pytest.mark.parametrize('func', [
        fibonacci_iterative,
        fibonacci_recursive,
        fibonacci_stack,
    ])
    @pytest.mark.parametrize('i,o', [
        (0, 0),
        (1, 1),
        (4, 3),
    ])
    def test_fibonacci(self, func, i, o):
        assert func(i) == o
