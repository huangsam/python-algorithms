from enum import Enum, auto
from heapq import heappop, heappush


class Direction(Enum):
    UP = auto()
    DOWN = auto()


def move_elevator(current_level, op_queue, direction):
    """Main driver for moving elevator."""
    if len(op_queue) == 0:
        return
    next_level = None
    priority = []
    visited = set()
    print("== {dir} from level {cur}".format(dir=direction, cur=current_level))
    bound = _get_bound(current_level, op_queue, direction)
    for pair in op_queue:
        pair_left, pair_right = pair
        if _spans(bound, pair) and _valid(pair, direction):
            heappush(priority, (_cost(current_level, pair_left), pair_left))
            heappush(priority, (_cost(current_level, pair_right), pair_right))
            visited.add(pair)
    op_queue = op_queue.difference(visited)
    while len(priority) > 0:
        _, next_level = heappop(priority)
        print("Arrived at this level: {nxt}".format(nxt=next_level))
    if len(op_queue) > 0:
        if next_level:
            move_elevator(next_level, op_queue, _opposite(direction))
        else:
            left, right = op_queue.pop()
            op_queue.add((left, right))
            move_elevator(left, op_queue, _opposite(direction))


def _get_bound(current_level, op_queue, direction) -> tuple[int, int]:
    """Calculate boundary given remaining operations."""
    if direction == Direction.UP:
        max_level = _get_max_level(op_queue)
        return current_level, max_level
    else:
        min_level = _get_min_level(op_queue)
        return min_level, current_level


def _valid(pair, direction) -> bool:
    """Determine whether pair is valid given direction."""
    if direction == Direction.UP:
        return pair[0] < pair[1]
    else:
        return pair[0] > pair[1]


def _cost(current, target) -> int:
    """Determine cost of entering target."""
    return abs(target - current)


def _get_max_level(op_queue) -> int:
    """Get maximum level for remaining operations."""
    return max(v for op in op_queue for v in op)


def _get_min_level(op_queue) -> int:
    """Get minimum level for remaining operations."""
    return min(v for op in op_queue for v in op)


def _spans(bound, pair) -> bool:
    """Determine whether boundary spans pair."""
    bl, br = bound
    pl, pr = pair
    return bl <= pl <= br and bl <= pr <= br


def _opposite(direction) -> Enum:
    """Simple toggle for direction."""
    return Direction.DOWN if direction == Direction.UP else Direction.UP


def main():
    op_queue = {(4, 8), (7, 4), (6, 3), (8, 9), (1, 2)}
    current_level = 5
    direction = Direction.UP
    move_elevator(current_level, op_queue, direction)


if __name__ == "__main__":
    main()
