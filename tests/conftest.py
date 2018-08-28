from random import randint

import pytest

from collection.list import ListNode


@pytest.fixture(scope='function', params=[50, 100, 400])
def array(request):
    return [randint(0, 100) for i in range(request.param)]


@pytest.fixture(scope='function')
def sorted_list(request):
    head = ListNode(0)
    node = head
    for i in range(1, 6):
        node.next_node = ListNode(i)
        node = node.next_node
    return head
