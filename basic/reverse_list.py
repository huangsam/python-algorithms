class ListNode(object):
    """List node has a value and references to other nodes."""

    def __init__(self, value=None):
        self.value = value
        self.next_node = None
        self.prev_node = None


def reverse_list(ll):
    cur_node = ll

    # 0 nodes
    if not cur_node:
        return None

    next_node = cur_node.next_node
    prev_node = None

    # n nodes
    while True:
        if next_node:
            next_next_node = next_node.next_node
            next_node = cur_node.next_node
            cur_node.next_node = prev_node
            prev_node = cur_node
            cur_node = next_node
            next_node = next_next_node
        else:
            cur_node.next_node = prev_node
            return cur_node


def create_list(n):
    head = ListNode(0)
    node = head
    for i in range(1, n):
        node.next_node = ListNode(i)
        node = node.next_node
    return head


def print_list(ll):
    current_node = ll
    while current_node:
        print(current_node.value)
        current_node = current_node.next_node


def main():
    head = create_list(10)
    print('=== before')
    print_list(head)
    new_head = reverse_list(head)
    print('=== after')
    print_list(new_head)


if __name__ == '__main__':
    main()
