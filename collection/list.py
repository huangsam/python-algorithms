class ListNode(object):
    """List node has a value and references to other nodes."""

    def __init__(self, value=None):
        self.value = value
        self.next_node = None
        self.prev_node = None
