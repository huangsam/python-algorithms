import bisect
import math


def sorted_squares(nums: list[int]) -> list[int]:
    """Find the squares of a sorted array in sorted order.

    Given a sorted array of integers (which may include negatives), return
    the squares of the numbers in sorted order.
    """
    left, right = 0, len(nums) - 1
    result = [0] * len(nums)
    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2
        if left_square > right_square:
            result[right - left] = left_square
            left += 1
        else:
            result[right - left] = right_square
            right -= 1
    return result


def find_kth_squared_value(nums: list[int], k: int) -> int:
    """Find the k-th smallest squared value in a sorted array.

    As a follow-up based on the previous function, find the k-th smallest
    squared value in the sorted array.
    """
    # 1. Define the search range for the ANSWER (the squared value)
    low = 0
    # The largest possible square is the square of the largest absolute value
    high = max(nums[0] ** 2, nums[-1] ** 2)

    result = high

    while low <= high:
        mid_val = (low + high) // 2

        # 2. Count squares <= mid_val
        # This is equivalent to finding elements in range [-sqrt(mid_val), sqrt(mid_val)]
        root = math.isqrt(mid_val)  # Integer square root

        # Find index of first element >= -root
        left_idx = bisect.bisect_left(nums, -root)
        # Find index of first element > root
        right_idx = bisect.bisect_right(nums, root)

        count = right_idx - left_idx

        # 3. Standard Binary Search logic
        if count >= k:
            result = mid_val
            high = mid_val - 1
        else:
            low = mid_val + 1

    return result
