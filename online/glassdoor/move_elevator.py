import heapq


def move_elevator(current_level, op_queue, direction):
    """Main driver for moving elevator."""
    if len(op_queue) == 0:
        return
    next_level = None
    priority = []
    visited = set()
    print(f'== {direction} from level {current_level}')
    bound = get_bound(current_level, op_queue, direction)
    for pair in op_queue:
        pair_left, pair_right = pair
        if spans(bound, pair) and valid(pair, direction):
            heapq.heappush(priority, (cost(current_level, pair_left), pair_left))
            heapq.heappush(priority, (cost(current_level, pair_right), pair_right))
            visited.add(pair)
    op_queue = op_queue.difference(visited)
    while len(priority) > 0:
        _, next_level = heapq.heappop(priority)
        print(f'Arrived at this level: {next_level}')
    if len(op_queue) > 0:
        if next_level:
            move_elevator(next_level, op_queue, opposite(direction))
        else:
            left, right = op_queue.pop()
            op_queue.add((left, right))
            move_elevator(left, op_queue, opposite(direction))


def get_bound(current_level, op_queue, direction):
    """Calculate boundary given remaining operations."""
    if direction.upper() == 'UP':
        max_level = get_max_level(op_queue)
        return (current_level, max_level)
    elif direction.upper() == 'DOWN':
        min_level = get_min_level(op_queue)
        return (min_level, current_level)


def valid(pair, direction):
    """Determine whether pair is valid given direction."""
    if direction.upper() == 'UP':
        return pair[0] < pair[1]
    else:
        return pair[0] > pair[1]


def cost(current, target):
    """Determine cost of entering target."""
    return abs(target - current)


def get_max_level(op_queue):
    """Get maximum level for remaining operations."""
    result = None
    for i, j in op_queue:
        if result is None:
            result = max(i, j)
        else:
            result = max(result, i, j)
    return result


def get_min_level(op_queue):
    """Get minimum level for remaining operations."""
    result = None
    for i, j in op_queue:
        if result is None:
            result = min(i, j)
        else:
            result = min(result, i, j)
    return result


def spans(bound, pair):
    """Determine whether boundary spans pair."""
    bl, br = bound
    pl, pr = pair
    return bl <= pl <= br and bl <= pr <= br


def opposite(direction):
    """Simple toggle for direction."""
    if direction.upper() == 'UP':
        return 'DOWN'
    else:
        return 'UP'


def main():
    op_queue = set([(4, 8), (7, 4), (6, 3), (7, 8), (8, 9), (1, 2)])
    current_level = 5
    direction = 'UP'
    move_elevator(current_level, op_queue, direction)


if __name__ == '__main__':
    main()
