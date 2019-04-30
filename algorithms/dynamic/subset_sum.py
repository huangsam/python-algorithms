def subset_sum_rec(nums, s):
    if s < 0:
        return False
    if s == 0:
        return True
    for num in nums:
        nums.remove(num)
        if subset_sum_rec(nums, s - num):
            return True
        nums.add(num)
    return False


# https://algorithms.tutorialhorizon.com//dynamic-programming-subset-sum-problem/
def subset_sum_dp(nums, s):
    nlen = len(nums)
    matrix = [[False] * (s + 1) for _ in range(nlen + 1)]
    snums = [_ for _ in sorted(nums)]
    for i in range(nlen + 1):
        matrix[i][0] = True
    for i in range(1, nlen + 1):
        for j in range(1, s + 1):
            matrix[i][j] = matrix[i - 1][j]
            if not matrix[i][j] and j >= snums[i - 1]:
                matrix[i][j] = matrix[i - 1][j - snums[i - 1]]
    return matrix[nlen][s]
