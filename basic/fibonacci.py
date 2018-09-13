def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    f, s = 0, 1
    for i in range(n - 1):
        result = f + s
        f, s = s, result
    return result


def fibonacci_stack(n):
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


def fibonacci_dp_bottom(n):
    mem = [0] * (n + 1)
    mem[1] = 1
    if n < 2:
        return mem[n]
    for i in range(2, n+1):
        mem[i] = mem[i-1] + mem[i-2]
    return mem[n]


def fibonacci_dp_top(n):
    return fibonacci_dp_top_work(n, {0: 0, 1: 1})


def fibonacci_dp_top_work(n, mem):
    if n in mem:
        return mem[n]
    mem[n] = fibonacci_dp_top_work(n-1, mem) + fibonacci_dp_top_work(n-2, mem)
    return mem[n]
