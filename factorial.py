def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial(n):
    stack = []
    result = 1
    while n > 0:
        stack.append(n)
        n -= 1
    while len(stack) > 0:
        result = result * stack.pop()
    return result
