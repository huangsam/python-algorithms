def bsearch_recursive(arr, t, lo, hi):
    if lo >= hi:
        return False
    mid = (lo + hi) // 2
    val = arr[mid]
    if val == t:
        return True
    elif val < t:
        return bsearch_recursive(arr, t, mid + 1, hi)
    return bsearch_recursive(arr, t, lo, mid)
