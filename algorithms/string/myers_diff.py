from typing import Any


def myers_diff(source: list | str, destination: list | str) -> list[tuple[str, Any]]:
    """Compute the minimal edit sequence using Myers Diff algorithm."""
    src_len, dst_len = len(source), len(destination)
    frontier = {1: 0}
    trace: list[dict[int, int]] = []

    for depth in range(src_len + dst_len + 1):
        v_copy = frontier.copy()
        for diagonal in range(-depth, depth + 1, 2):
            if diagonal == -depth or (diagonal != depth and v_copy[diagonal - 1] < v_copy[diagonal + 1]):
                x = v_copy[diagonal + 1]
            else:
                x = v_copy[diagonal - 1] + 1
            y = x - diagonal

            while x < src_len and y < dst_len and source[x] == destination[y]:
                x, y = x + 1, y + 1
            frontier[diagonal] = x

            if x >= src_len and y >= dst_len:
                return _backtrack(src_len, dst_len, trace + [frontier.copy()], source, destination)
        trace.append(frontier.copy())
    return []


def _backtrack(src_len, dst_len, trace, source, destination):
    """Backtrack through the trace to construct the edit script."""
    x, y = src_len, dst_len
    script = []

    for depth in range(len(trace) - 1, -1, -1):
        trace[depth]
        diagonal = x - y
        prev_frontier = trace[depth - 1] if depth > 0 else {1: 0}

        if diagonal == -depth or (diagonal != depth and prev_frontier[diagonal - 1] < prev_frontier[diagonal + 1]):
            prev_diagonal = diagonal + 1
        else:
            prev_diagonal = diagonal - 1

        prev_x = prev_frontier[prev_diagonal]
        prev_y = prev_x - prev_diagonal

        while x > prev_x and y > prev_y:
            script.append(("keep", source[x - 1]))
            x, y = x - 1, y - 1

        if depth > 0:
            if x > prev_x:
                script.append(("delete", source[x - 1]))
            else:
                script.append(("insert", destination[y - 1]))
            x, y = prev_x, prev_y

    return script[::-1]
