from collection.stack import Stack


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

    def test_size(self):
        stack = Stack()
        for i in range(100):
            stack.push(i)
        for i in range(20):
            stack.pop()
        assert stack.size() == 80
