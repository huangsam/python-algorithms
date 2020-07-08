from typing import Dict, List, Tuple

from algorithms.constants import MAX_INT

IndexCache = Dict[Tuple[int, int, int], int]


# https://www.geeksforgeeks.org/painters-partition-problem/
def split_sum(arr: List[int], k: int):
    return split_sum_wh(arr, k, 0, len(arr), {})


def split_sum_wh(arr: List[int], k: int, left: int, right: int, cache: IndexCache):
    if (k, left, right) in cache:
        return cache[(k, left, right)]
    if k == 1:
        result = cache[(k, left, right)] = sum(arr[left:right])
        return result
    result = MAX_INT
    for i in range(left + 1, right):
        lval = cache[(k, left, i)] = sum(arr[left:i])
        rval = cache[(k - 1, i, right)] = split_sum_wh(arr, k - 1, i, right, cache)
        result = min(result, max(lval, rval))
    return result
