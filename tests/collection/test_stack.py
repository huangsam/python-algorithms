import pytest

from algorithms.collection.stack import FunkyStack, Stack


@pytest.mark.stack
def test_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)


@pytest.mark.stack
def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2


@pytest.mark.stack
def test_max_push():
    stack = Stack()
    stack.push(4)
    stack.push(3)
    assert stack.max() == 4


@pytest.mark.stack
def test_max_pop():
    stack = Stack()
    stack.push(4)
    stack.push(5)
    assert stack.max() == 5
    stack.push(5)
    stack.pop()
    assert stack.max() == 5
    stack.pop()
    assert stack.max() == 4


@pytest.mark.stack
def test_max_pop_error():
    stack = Stack()
    stack.push(4)
    assert stack.max() == 4
    stack.pop()
    with pytest.raises(ValueError):
        stack.max()


@pytest.mark.stack
def test_size():
    stack = Stack()
    for i in range(100):
        stack.push(i)
    for i in range(20):
        stack.pop()
    assert stack.size() == 80


@pytest.mark.stack
def test_push():
    stack = FunkyStack()
    stack.push(1)
    stack.push(2)


@pytest.mark.stack
def test_pop():
    stack = FunkyStack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.size() == 1
    assert stack.pop() == 1
    assert stack.size() == 0
