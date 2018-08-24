def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci(n):
    if n < 0:
        raise Exception('Invalid number')
    if n < 2:
        return n
    f, s = 0, 1
    for i in range(n):
        result = f + s
        f, s = s, result
    return result


def fibonacci(n):
    if n < 2:
        return max(0, n)
    stack = [0, 1]
    i = 1
    while i < n:
        s = stack.pop()
        f = stack.pop()
        stack.append(s)
        stack.append(f + s)
        i += 1
    return stack.pop()
