import pytest

from algorithms.math.fibonacci import fibonacci_dp_bottom, fibonacci_dp_top, fibonacci_iterative, fibonacci_recursive, fibonacci_stack


@pytest.mark.math
@pytest.mark.dynamic
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
@pytest.mark.parametrize("i,o", [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8)])
def test_fibonacci(func, i, o):
    assert func(i) == o
