from typing import Dict


def fibonacci_recursive(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    f, s = 0, 1
    for i in range(n - 1):
        result = f + s
        f, s = s, result
    return result


def fibonacci_stack(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    stack = [0, 1]
    i = 1
    while i < n:
        s = stack.pop()
        f = stack.pop()
        stack.append(s)
        stack.append(f + s)
        i += 1
    return stack.pop()


def fibonacci_dp_bottom(n: int):
    mem = [0] * max(2, n + 1)
    mem[1] = 1
    if n < 2:
        return mem[n]
    for i in range(2, n + 1):
        mem[i] = mem[i - 1] + mem[i - 2]
    return mem[n]


def fibonacci_dp_top(n: int):
    return _fibonacci_dp_top_work(n, {0: 0, 1: 1})


def _fibonacci_dp_top_work(n: int, mem: Dict[int, int]):
    if n in mem:
        return mem[n]
    mem[n] = _fibonacci_dp_top_work(n - 1, mem) + _fibonacci_dp_top_work(n - 2, mem)
    return mem[n]
