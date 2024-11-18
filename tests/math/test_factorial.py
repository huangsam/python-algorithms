import pytest

from algorithms.math.factorial import factorial_dp_bottom, factorial_dp_top, factorial_recursive, factorial_stack


@pytest.mark.math
@pytest.mark.dynamic
@pytest.mark.parametrize(
    "func",
    [
        factorial_recursive,
        factorial_stack,
        factorial_dp_bottom,
        factorial_dp_top,
    ],
)
@pytest.mark.parametrize("i,o", [(0, 1), (1, 1), (2, 2), (3, 6), (4, 24), (5, 120)])
def test_factorial(func, i: int, o: int):
    assert func(i) == o
