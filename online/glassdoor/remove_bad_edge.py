def remove_bad_edge(root):
    seen = set()
    cur = root
    par = None
    direction = None
    remove_bad_edge_work(cur, par, direction, seen)


def remove_bad_edge_work(cur, par, direction, seen):
    if cur is None:
        return

    if cur.val in seen:
        if direction == 'l':
            par.left = None
            return
        if direction == 'r':
            par.right = None
            return
    else:
        seen.add(cur.val)

    remove_bad_edge_work(cur.left, cur, 'l', seen)
    remove_bad_edge_work(cur.right, cur, 'r', seen)
