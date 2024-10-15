from enum import Enum, auto

from algorithms.collections.tree import TreeNode


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()


def remove_bad_edge(root: TreeNode):
    seen: set = set()
    cur: TreeNode | None = root
    par: TreeNode | None = None
    direction: Direction | None = None
    _remove_bad_edge_work(cur, par, direction, seen)


def _remove_bad_edge_work(
    cur: TreeNode | None,
    par: TreeNode | None,
    direction: Direction | None,
    seen: set,
):
    if cur is None:
        return

    if id(cur) in seen:
        if direction == Direction.LEFT and par:
            par.left = None
            return
        if direction == Direction.RIGHT and par:
            par.right = None
            return
    else:
        seen.add(id(cur))

    _remove_bad_edge_work(cur.left, cur, Direction.LEFT, seen)
    _remove_bad_edge_work(cur.right, cur, Direction.RIGHT, seen)
