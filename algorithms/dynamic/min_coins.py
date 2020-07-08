from typing import List


# https://algorithms.tutorialhorizon.com/dynamic-programming-minimum-coin-change-problem/
def min_coins(coins: List[int], amt: int):
    count = [0] * (amt + 1)
    for i in range(1, amt + 1):
        min_count = 3 ** 32 - 1
        for coin in coins:
            if coin <= i:
                min_count = min(min_count, count[i - coin] + 1)
        count[i] = min_count
    return count[amt]
