import pytest

from collection.stack import (
    Stack,
    FunkyStack,
)


class TestStack(object):

    def test_push(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2

    def test_max_push(self):
        stack = Stack()
        stack.push(4)
        stack.push(3)
        assert stack.max() == 4

    def test_max_pop(self):
        stack = Stack()
        stack.push(4)
        stack.push(5)
        assert stack.max() == 5
        stack.push(5)
        stack.pop()
        assert stack.max() == 5
        stack.pop()
        assert stack.max() == 4

    def test_max_pop_error(self):
        stack = Stack()
        stack.push(4)
        assert stack.max() == 4
        stack.pop()
        with pytest.raises(ValueError):
            stack.max()

    def test_size(self):
        stack = Stack()
        for i in range(100):
            stack.push(i)
        for i in range(20):
            stack.pop()
        assert stack.size() == 80


class TestFunkyStack(object):

    def test_push(self):
        stack = FunkyStack()
        stack.push(1)
        stack.push(2)

    def test_pop(self):
        stack = FunkyStack()
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        assert stack.size() == 1
        assert stack.pop() == 1
        assert stack.size() == 0
