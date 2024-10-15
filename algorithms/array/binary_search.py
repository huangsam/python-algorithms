def binary_search_recursive(arr: list[int], t: int):
    return _binary_search_recursive_work(arr, t, 0, len(arr) - 1)


def _binary_search_recursive_work(arr: list[int], t: int, lo: int, hi: int):
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    val = arr[mid]
    if val == t:
        return mid
    elif val < t:
        return _binary_search_recursive_work(arr, t, mid + 1, hi)
    return _binary_search_recursive_work(arr, t, lo, mid - 1)


# https://en.wikipedia.org/wiki/Binary_search_algorithm
def binary_search_iterative(arr: list[int], t: int):
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
