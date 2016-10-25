#!/usr/bin/env python
"""Helper routines"""


def copy_array(a, begin, end, b):
    for k in range(begin, end):
        b[k] = a[k]


"""Mergesort routines"""


def mergesort(a, style="topdown"):
    n = len(a)
    # copy new array
    b = [0 for i in range(n)]
    if style == "bottomup":
        mergesort_bottomup(a, b, n)
    elif style == "topdown":
        mergesort_topdown(a, b, n)
    else:
        raise Exception("Invalid style - " + style)


# https://en.wikipedia.org/wiki/Merge_sort#Top-down_implementation
def mergesort_topdown(a, b, n):
    copy_array(a, 0, n, b)
    split_merge_topdown(b, 0, n, a)


def split_merge_topdown(b, begin, end, a):
    if (end - begin < 2):
        return
    middle = int((end + begin) / 2)
    # sort left into B
    split_merge_topdown(a, begin, middle, b)
    # sort right into B
    split_merge_topdown(a, middle, end, b)
    # merge resulting runs from B into A
    merge(b, begin, middle, end, a)


# https://en.wikipedia.org/wiki/Merge_sort#Bottom-up_implementation
def mergesort_bottomup(a, b, n):
    width = 1
    while width < n:
        i = 0
        while i < n:
            merge(a, i, min(i+width, n), min(i+2*width, n), b)
            i += 2 * width
        copy_array(b, 0, n, a)
        width *= 2


# Common merge routine
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


"""Main routine"""


def main():
    A = [1, 10, 4, 5, 4, 18, 17, 20, 3, 16]
    print("before:", A)
    mergesort(A)
    print("after:", A)

if __name__ == '__main__':
    main()
