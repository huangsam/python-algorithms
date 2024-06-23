from algorithms.collections.tree import TreeNode


def remove_bad_edge(root: TreeNode):
    seen: set = set()
    cur: TreeNode | None = root
    par: TreeNode | None = None
    direction: str | None = None
    _remove_bad_edge_work(cur, par, direction, seen)


def _remove_bad_edge_work(
    cur: TreeNode | None,
    par: TreeNode | None,
    direction: str | None,
    seen: set,
):
    if cur is None:
        return

    if cur.value in seen:
        if direction == "l" and par:
            par.left = None
            return
        if direction == "r" and par:
            par.right = None
            return
    else:
        seen.add(cur.value)

    _remove_bad_edge_work(cur.left, cur, "l", seen)
    _remove_bad_edge_work(cur.right, cur, "r", seen)
