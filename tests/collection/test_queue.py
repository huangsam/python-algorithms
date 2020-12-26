import pytest

from algorithms.collection.queue import FunkyQueue, Queue


@pytest.mark.queue
def test_push():
    queue = Queue()
    queue.push(1)
    queue.push(2)


@pytest.mark.queue
def test_pop():
    queue = Queue()
    queue.push(1)
    queue.push(2)
    assert queue.pop() == 1


@pytest.mark.queue
def test_size():
    queue = Queue()
    for i in range(100):
        queue.push(i)
    for i in range(20):
        queue.pop()
    assert queue.size() == 80


@pytest.mark.queue
def test_push():
    queue = FunkyQueue()
    queue.push(1)
    queue.push(2)


@pytest.mark.queue
def test_pop():
    queue = FunkyQueue()
    queue.push(1)
    queue.push(2)
    assert queue.pop() == 1


@pytest.mark.queue
def test_size():
    queue = FunkyQueue()
    for i in range(100):
        queue.push(i)
    for i in range(20):
        queue.pop()
    assert queue.size() == 80
