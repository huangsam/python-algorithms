from basic.factorial import (
    factorial_recursive,
    factorial_stack,
)


class TestFactorial(object):

    def test_factorial_recursive(self):
        assert factorial_recursive(4) == 24

    def test_factorial_stack(self):
        assert factorial_stack(4) == 24
