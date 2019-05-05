# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
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


def search_min(nums):
    lo = 0
    hi = len(nums) - 1
    while lo < hi:
        while lo < len(nums) and nums[lo] == nums[lo + 1]:
            lo = lo + 1
        while hi >= 0 and nums[hi] == nums[hi - 1]:
            hi = hi - 1
        mid = (lo + hi) // 2
        if nums[lo] <= nums[mid] <= nums[hi]:
            return nums[lo]
        if nums[lo] > nums[mid]:
            lo = lo + 1
            hi = mid
        if nums[mid] > nums[hi]:
            lo = mid + 1
    return nums[lo]
