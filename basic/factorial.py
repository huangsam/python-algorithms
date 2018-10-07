def factorial_recursive(n):
    if n < 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def factorial_stack(n):
    stack = []
    result = 1
    while n > 0:
        stack.append(n)
        n -= 1
    while len(stack) > 0:
        result = result * stack.pop()
    return result


def factorial_dp_bottom(n):
    answers = [1] * max(1, n + 1)
    for i in range(2, n + 1):
        answers[i] = i * answers[i - 1]
    return answers[n]


def factorial_dp_top(n):
    return factorial_dp_top_work(n, {0: 1, 1: 1})


def factorial_dp_top_work(n, answers):
    if n in answers:
        return answers[n]
    answers[n] = n * factorial_dp_top_work(n - 1, answers)
    return answers[n]
