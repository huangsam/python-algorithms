import math


def egg_drop(n, k):
    if k < 2 or n == 1:
        return k
    minimum = math.inf
    for x in range(1, k):
        below = egg_drop(n - 1, x - 1)
        above = egg_drop(n, k - x)
        minimum = min(max(below, above), minimum)
    return 1 + minimum


# https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/
def egg_drop_optimal(n, k):
    answers = [[0] * (k + 1) for i in range(n + 1)]
    # 1 trial, 1 floor and 0 trials, 0 floors
    for i in range(1, n + 1):
        answers[i][0] = 0
        answers[i][1] = 1
    # 1 egg with j floors
    for j in range(1, k + 1):
        answers[1][j] = j
    # optimal substructure
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            answers[i][j] = math.inf
            for x in range(1, j + 1):
                res = 1 + max(answers[i - 1][x - 1], answers[i][j - x])
                answers[i][j] = min(res, answers[i][j])
    return answers[n][k]
