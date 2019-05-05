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
    return search_min_wh(nums, 0, len(nums) - 1)


def search_min_wh(nums, lo, hi):
    mid = (lo + hi) // 2

    if lo == hi:
        return nums[lo]

    if nums[lo] <= nums[mid] <= nums[hi]:
        return nums[lo]

    if nums[lo] > nums[mid]:
        return search_min_wh(nums, lo + 1, mid)

    if nums[mid] > nums[hi]:
        return search_min_wh(nums, mid + 1, hi)
