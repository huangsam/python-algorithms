def search_rotated(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if target == nums[mid]:
            return True
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target <= nums[mid]:
                lo, hi = lo, mid - 1
            else:
                lo, hi = mid + 1, hi
        else:
            if nums[mid] <= target <= nums[hi]:
                lo, hi = mid + 1, hi
            else:
                lo, hi = lo, mid - 1
    return False
