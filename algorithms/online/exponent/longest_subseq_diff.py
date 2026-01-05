def longest_subseq_diff(nums: list[int], target: int) -> int:
    """
    Given an array of integers, return the length of the longest subsequence
    where the difference between any two elements is less than the target.
    """
    if not nums:
        return 0
    sorted_nums = sorted(nums)
    left = 0
    max_length = 1  # At least one element will always satisfy the condition
    for right in range(len(sorted_nums)):
        # Shrink window from the left until condition is met
        while left <= right and sorted_nums[right] - sorted_nums[left] >= target:
            left += 1
        # Check if the window is valid (important if target <= 0)
        if left <= right:
            max_length = max(max_length, right - left + 1)
    return max_length
