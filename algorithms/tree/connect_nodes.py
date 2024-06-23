from typing import Any, cast

from algorithms.collections.tree import TreeNode


class NextNode(TreeNode):
    def __init__(self, value: Any):
        super().__init__(value)
        self.next: NextNode | None = None


def next_node(node: TreeNode) -> NextNode:
    return cast(NextNode, node)


def connect_nodes_double(root: NextNode):
    cur_nodes: list[NextNode] = [root]
    next_nodes: list[NextNode] = []
    while len(cur_nodes) > 0 or len(next_nodes) > 0:
        prev_n = None
        while len(cur_nodes) > 0:
            n = cur_nodes.pop(0)
            if n.right:
                next_nodes.append(next_node(n.right))
            if n.left:
                next_nodes.append(next_node(n.left))
            n.next = prev_n
            prev_n = n
        cur_nodes, next_nodes = next_nodes, cur_nodes


# https://www.geeksforgeeks.org/connect-nodes-level-level-order-traversal/
def connect_nodes_single(root: NextNode):
    queue: list[NextNode | None] = [root, None]
    while len(queue) > 0:
        n = queue.pop(0)
        if n:
            n.next = queue[0]
            if n.left:
                queue.append(next_node(n.left))
            if n.right:
                queue.append(next_node(n.right))
        elif len(queue) > 0:
            queue.append(None)
