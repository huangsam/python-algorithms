from basic.fibonacci import (
    fibonacci_recursive,
    fibonacci_iterative,
    fibonacci_stack,
)


class TestFibonacci(object):

    def test_fibonacci_recursive(self):
        assert fibonacci_recursive(4) == 3

    def test_fibonacci_iterative(self):
        assert fibonacci_iterative(4) == 3

    def test_fibonacci_stack(self):
        assert fibonacci_stack(4) == 3
