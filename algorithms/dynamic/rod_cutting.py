from typing import List


def rod_cutting_rec(n: int, prices: List[int]):
    if n == 0:
        return 0
    if n == 1:
        return prices[0]
    result = -1
    for i in range(1, n + 1):
        cut = prices[i - 1]
        remainder = rod_cutting_rec(n - i, prices)
        result = max(cut + remainder, result)
    return result


# https://algorithms.tutorialhorizon.com/dynamic-programming-rod-cutting-problem/
def rod_cutting_dp(n: int, prices: List[int]):
    revenue = [0] * max(2, n + 1)
    revenue[1] = prices[0]
    if n < 2:
        return revenue[n]
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            revenue[i] = max(prices[j - 1] + revenue[i - j], revenue[i])
    return revenue[n]
