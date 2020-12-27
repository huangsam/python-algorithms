from typing import Optional, Set

from algorithms.collections.tree import TreeNode


def remove_bad_edge(root: TreeNode):
    seen: Set = set()
    cur: Optional[TreeNode] = root
    par: Optional[TreeNode] = None
    direction: Optional[str] = None
    _remove_bad_edge_work(cur, par, direction, seen)


def _remove_bad_edge_work(
    cur: Optional[TreeNode],
    par: Optional[TreeNode],
    direction: Optional[str],
    seen: Set,
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
