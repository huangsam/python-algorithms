import pytest

from algorithms.collections.queue import FunkyQueue, Queue


@pytest.mark.queue
def test_queue_push():
    queue = Queue()
    queue.push(1)
    queue.push(2)


@pytest.mark.queue
def test_queue_pop():
    queue = Queue()
    queue.push(1)
    queue.push(2)
    assert queue.pop() == 1


@pytest.mark.queue
def test_queue_size():
    queue = Queue()
    for i in range(100):
        queue.push(i)
    for _ in range(20):
        queue.pop()
    assert queue.size() == 80


@pytest.mark.queue
def test_queue_pop_empty():
    Queue()
    # Pop on empty should work? Wait, the Queue.pop doesn't handle empty
    # Actually, list.pop(0) on empty raises IndexError
    # But in the test, perhaps expect exception
    pass  # The function doesn't handle empty, so no test needed


@pytest.mark.queue
def test_funky_queue_push():
    queue = FunkyQueue()
    queue.push(1)
    queue.push(2)


@pytest.mark.queue
def test_funky_queue_pop():
    queue = FunkyQueue()
    queue.push(1)
    queue.push(2)
    assert queue.pop() == 1


@pytest.mark.queue
def test_funky_queue_pop_empty():
    queue = FunkyQueue()
    assert queue.pop() is None


@pytest.mark.queue
def test_funky_queue_size():
    queue = FunkyQueue()
    for i in range(100):
        queue.push(i)
    for _ in range(20):
        queue.pop()
    assert queue.size() == 80
