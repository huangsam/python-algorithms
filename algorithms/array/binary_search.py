from typing import Any, List


def binary_search_recursive(arr: List[Any], t: Any):
    return binary_search_recursive_work(arr, t, 0, len(arr) - 1)


def binary_search_recursive_work(arr: List[Any], t: Any, lo: int, hi: int):
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    val = arr[mid]
    if val == t:
        return mid
    elif val < t:
        return binary_search_recursive_work(arr, t, mid + 1, hi)
    return binary_search_recursive_work(arr, t, lo, mid - 1)


# https://en.wikipedia.org/wiki/Binary_search_algorithm
def binary_search_iterative(arr: List[Any], t: Any):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = arr[mid]
        if val == t:
            return mid
        elif val < t:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
