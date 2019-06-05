from algorithms.constants import MAX_INT


# https://www.geeksforgeeks.org/painters-partition-problem/
def split_sum(arr, k):
    return split_sum_wh(arr, k, 0, len(arr), {})


def split_sum_wh(arr, k, l, r, cache):
    if (k, l, r) in cache:
        return cache[(k, l, r)]
    if k == 1:
        result = cache[(k, l, r)] = sum(arr[l:r])
        return result
    result = MAX_INT
    for i in range(l + 1, r):
        lval = cache[(k, l, i)] = sum(arr[l:i])
        rval = cache[(k - 1, i, r)] = split_sum_wh(arr, k - 1, i, r, cache)
        result = min(result, max(lval, rval))
    return result
