def connect_nodes_double(root):
    cur_nodes = [root]
    next_nodes = []
    while len(cur_nodes) > 0 or len(next_nodes) > 0:
        prev_n = None
        while len(cur_nodes) > 0:
            n = cur_nodes.pop(0)
            if n.right:
                next_nodes.append(n.right)
            if n.left:
                next_nodes.append(n.left)
            n.next = prev_n
            prev_n = n
        while len(next_nodes) > 0:
            cur_nodes.append(next_nodes.pop(0))


# https://www.geeksforgeeks.org/connect-nodes-level-level-order-traversal/
def connect_nodes_single(root):
    queue = [root, None]
    while len(queue) > 0:
        n = queue.pop(0)
        if n:
            n.next = queue[0]
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
        elif len(queue) > 0:
            queue.append(None)
