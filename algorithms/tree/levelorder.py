from collections import deque
from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any

from algorithms.collections.tree import TreeNode


def levelorder_basic(root: TreeNode | None) -> list[Any]:
    """This assumes that you don't care about the exact height you are at."""
    if root is None:
        return []
    result = []
    queue = deque([root])
    while len(queue) > 0:
        c = queue.popleft()
        result.append(c.value)
        if c.left is not None:
            queue.append(c.left)
        if c.right is not None:
            queue.append(c.right)
    return result


@dataclass
class LevelItem:
    node: TreeNode
    level: int


def levelorder_height_with_node(root: TreeNode | None) -> Iterable[LevelItem]:
    """Process the exact level i based on node information."""
    if root is None:
        return
    queue: deque[LevelItem] = deque([LevelItem(root, 0)])
    while len(queue) > 0:
        c = queue.popleft()
        yield c
        if c.node.left is not None:
            queue.append(LevelItem(c.node.left, c.level + 1))
        if c.node.right is not None:
            queue.append(LevelItem(c.node.right, c.level + 1))


def levelorder_height_with_queues(root: TreeNode | None) -> Iterable[LevelItem]:
    """This is similar to above except that it uses two queues.

    The approach is slightly more complicated but it has the advantage of not
    needing to store the level information with each node. Rather, the current
    node level is stored in a separate variable.
    """
    if root is None:
        return
    current_level: deque[TreeNode] = deque([root])
    next_level: deque[TreeNode] = deque()
    level = 0
    while len(current_level) > 0:
        c = current_level.popleft()
        yield LevelItem(c, level)
        if c.left is not None:
            next_level.append(c.left)
        if c.right is not None:
            next_level.append(c.right)
        if len(current_level) == 0:
            current_level, next_level = next_level, current_level
            level += 1
