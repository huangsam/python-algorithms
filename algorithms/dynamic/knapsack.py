def knapsack_rec(weight, items):
    return knapsack_wh(weight, items, len(items), set(), {})


def knapsack_wh(weight, items, n, picked, cache):
    result = 0
    if n == 0 or weight == 0:
        return 0
    if (n, weight) in cache:
        return cache[(n, weight)]
    for ix, val in enumerate(items):
        if ix in picked:
            continue
        iw, iv = items[ix]
        if iw <= weight:
            picked.add(ix)
            used = iv + knapsack_wh(weight - iw, items, n - 1, picked, cache)
            not_used = knapsack_wh(weight, items, n - 1, picked, cache)
            result = max(result, used, not_used)
            picked.remove(ix)
        else:
            not_used = knapsack_wh(weight, items, n - 1, picked, cache)
            result = max(result, not_used)
    cache[(n, weight)] = result
    return result


# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
def knapsack_dp(weight, items):
    N = len(items) + 1
    W = weight + 1
    total = [[0] * W for _ in range(N)]
    for i in range(1, N):
        for j in range(1, W):
            iw, iv = items[i - 1]
            not_used = total[i - 1][j]
            if iw <= j:
                used = iv + total[i - 1][j - iw]
                total[i][j] = max(used, not_used)
            else:
                total[i][j] = not_used
    return total[-1][-1]
