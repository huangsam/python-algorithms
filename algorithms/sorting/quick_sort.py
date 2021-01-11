# https://en.wikipedia.org/wiki/Quicksort
def sort(arr, iterative=True):
    if iterative is True:
        quicksort_iterative(arr, 0, len(arr) - 1)
    else:
        quicksort_recursive(arr, 0, len(arr) - 1)


def _partition_lomuto(arr, lo, hi):
    i = lo
    pivot = arr[hi]
    for j in range(lo, hi):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i


def quicksort_iterative(arr, lo, hi):
    stack = [(lo, hi)]
    while len(stack) > 0:
        lo, hi = stack.pop()
        if lo < hi:
            p = _partition_lomuto(arr, lo, hi)
            stack.append((lo, p - 1))
            stack.append((p + 1, hi))


def quicksort_recursive(arr, lo, hi):
    if lo < hi:
        p = _partition_lomuto(arr, lo, hi)
        quicksort_recursive(arr, lo, p - 1)
        quicksort_recursive(arr, p + 1, hi)
