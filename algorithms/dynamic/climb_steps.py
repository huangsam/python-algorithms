# https://www.geeksforgeeks.org/count-ways-reach-nth-stair/
def climb_steps(n: int, steps: list[int]):
    """Calculates the number of ways to climb n steps with given step sizes."""
    max_step = max(steps)
    answers = [0] * max(max_step + 1, n + 1)
    for step in steps:
        answers[step] = 1
    for i in range(1, n + 1):
        for step in steps:
            if (i - step) >= 0:
                answers[i] += answers[i - step]
    return answers[n]
