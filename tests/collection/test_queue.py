from collection.queue import Queue


class TestQueue(object):

    def test_push(self):
        queue = Queue()
        queue.push(1)
        queue.push(2)

    def test_pop(self):
        queue = Queue()
        queue.push(1)
        assert queue.pop() == 1

    def test_size(self):
        queue = Queue()
        for i in range(100):
            queue.push(i)
        for i in range(20):
            queue.pop()
        assert queue.size() == 80
