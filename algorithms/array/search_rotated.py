# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
def search_one(nums: list[int], target: int):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if target == nums[mid]:
            return True
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target <= nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] <= target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return False


# https://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/
def search_min(nums: list[int]):
    lo = 0
    hi = len(nums) - 1
    while lo < hi:
        while lo < len(nums) and nums[lo] == nums[lo + 1]:
            lo = lo + 1
        while hi >= 0 and nums[hi] == nums[hi - 1]:
            hi = hi - 1
        mid = (lo + hi) // 2
        if mid < hi and nums[mid + 1] < nums[mid]:
            return nums[mid + 1]
        if mid > lo and nums[mid] < nums[mid - 1]:
            return nums[mid]
        if nums[hi] > nums[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return nums[lo]
