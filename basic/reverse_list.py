class ListNode(object):
    """List node has a value and references to other nodes."""

    def __init__(self, value=None):
        self.value = value
        self.next_node = None
        self.prev_node = None


def reverse_list(ll):
    cur_node = ll
    next_node = None
    prev_node = None
    while cur_node:
        next_node = cur_node.next_node
        cur_node.next_node = prev_node
        prev_node = cur_node
        cur_node = next_node
    return prev_node
