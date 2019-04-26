# https://en.wikipedia.org/wiki/Merge_sort
def sort(a):
    n = len(a)
    # create new array
    b = [0 for i in range(n)]
    mergesort_topdown(a, b, n)


def mergesort_topdown(a, b, n):
    copy_array(a, 0, n, b)
    split_merge_topdown(b, 0, n, a)


def split_merge_topdown(b, begin, end, a):
    if end - begin < 2:
        return
    middle = (end + begin) // 2
    # sort left into B
    split_merge_topdown(a, begin, middle, b)
    # sort right into B
    split_merge_topdown(a, middle, end, b)
    # merge resulting runs from B into A
    merge(b, begin, middle, end, a)


def merge(a, left, right, end, b):
    i, j = left, right
    # while elements in left or right runs
    for k in range(left, end):
        # left run head exists and is <= existing right run head
        if i < right and (j >= end or a[i] <= a[j]):
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1


def copy_array(a, begin, end, b):
    for k in range(begin, end):
        b[k] = a[k]
