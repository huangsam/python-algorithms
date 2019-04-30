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
