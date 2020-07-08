from typing import Set


def subset_sum_rec(nums: Set[int], s: int):
    if s < 0:
        return False
    if s == 0:
        return True
    for num in nums.copy():
        nums.remove(num)
        if subset_sum_rec(nums, s - num):
            return True
        nums.add(num)
    return False


# https://algorithms.tutorialhorizon.com/dynamic-programming-subset-sum-problem/
def subset_sum_dp(nums: Set[int], s: int):
    nlen = len(nums)
    snums = [_ for _ in sorted(nums)]
    using = [[False] * (s + 1) for _ in range(nlen + 1)]
    for i in range(nlen + 1):
        using[i][0] = True
    for i in range(1, nlen + 1):
        for j in range(1, s + 1):
            using[i][j] = using[i - 1][j]
            if not using[i][j] and j >= snums[i - 1]:
                using[i][j] = using[i - 1][j - snums[i - 1]]
    return using[nlen][s]
