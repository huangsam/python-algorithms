def connect_nodes(root):
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
