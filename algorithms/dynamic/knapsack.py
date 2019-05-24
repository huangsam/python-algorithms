# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
def knapsack_dp(weight, items):
    N = len(items) + 1
    W = weight + 1
    answers = [[0] * W for _ in range(N)]
    for i in range(1, N):
        for j in range(1, W):
            iw, iv = items[i - 1]
            not_used = answers[i - 1][j]
            if iw <= j:
                used = iv + answers[i - 1][j - iw]
                answers[i][j] = max(used, not_used)
            else:
                answers[i][j] = not_used
    return answers[-1][-1]
