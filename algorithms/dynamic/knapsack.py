Item = tuple[int, int]
ItemList = list[Item]
ItemCache = dict[Item, int]


def knapsack_binary_rec(weight: int, items: ItemList):
    return _knapsack_binary_wh(weight, items, len(items), set(), {})


def _knapsack_binary_wh(weight: int, items: ItemList, n: int, picked: set, cache: ItemCache):
    result = 0
    if n == 0 or weight == 0:
        return 0
    if (n, weight) in cache:
        return cache[(n, weight)]
    for ix, _val in enumerate(items):
        if ix in picked:
            continue
        iw, iv = items[ix]
        if iw <= weight:
            picked.add(ix)
            used = iv + _knapsack_binary_wh(weight - iw, items, n - 1, picked, cache)
            not_used = _knapsack_binary_wh(weight, items, n - 1, picked, cache)
            result = max(result, used, not_used)
            picked.remove(ix)
        else:
            not_used = _knapsack_binary_wh(weight, items, n - 1, picked, cache)
            result = max(result, not_used)
    cache[(n, weight)] = result
    return result


# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
def knapsack_binary_dp(weight: int, items: ItemList):
    N = len(items) + 1
    W = weight + 1
    value = [[0] * W for _ in range(N)]
    for i in range(1, N):
        for j in range(1, W):
            iw, iv = items[i - 1]
            not_used = value[i - 1][j]
            if iw <= j:
                used = iv + value[i - 1][j - iw]
                value[i][j] = max(used, not_used)
            else:
                value[i][j] = not_used
    return value[-1][-1]


# https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/
def knapsack_infinite(weight: int, items: ItemList):
    value = [0] * (weight + 1)
    for i in range(1, weight + 1):
        for iw, iv in items:
            if iw <= i:
                value[i] = max(value[i], iv + value[i - iw])
    return value[-1]
