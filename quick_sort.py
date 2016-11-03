#!/usr/bin/env python


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


# https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
def hoare(arr, lo, hi):
    pivot = arr[lo]
    i = lo - 1
    j = hi + 1
    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        while True:
            j -= 1
            if arr[j] <= pivot:
                break
        if i >= j:
            return j
        swap(arr, i, j)


# https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme
def lomuto(arr, lo, hi):
    i = lo
    pivot = arr[hi]
    for j in range(lo, hi):
        if arr[j] <= pivot:
            swap(arr, i, j)
            i += 1
    swap(arr, i, hi)
    return i


def partition_iterative(arr, lo, hi, stack, scheme="lomuto"):
    p = None
    if scheme == "lomuto":
        p = lomuto(arr, lo, hi)
        stack.append((lo, p - 1))
    elif scheme == "hoare":
        p = hoare(arr, lo, hi)
        stack.append((lo, p))
    else:
        raise Exception("Invalid partition scheme - " + scheme)
    stack.append((p + 1, hi))


def partition_recursive(arr, lo, hi, scheme="lomuto"):
    p = None
    if scheme == "lomuto":
        p = lomuto(arr, lo, hi)
        quicksort_recursive(arr, lo, p - 1, scheme)
    elif scheme == "hoare":
        p = hoare(arr, lo, hi)
        quicksort_recursive(arr, lo, p, scheme)
    else:
        raise Exception("Invalid partition scheme - " + scheme)
    quicksort_recursive(arr, p + 1, hi, scheme)


def quicksort_iterative(arr, lo, hi, scheme):
    stack = [(lo, hi)]
    while len(stack) > 0:
        lo, hi = stack.pop()
        if lo < hi:
            partition_iterative(arr, lo, hi, stack, scheme)


def quicksort_recursive(arr, lo, hi, scheme):
    if lo < hi:
        partition_recursive(arr, lo, hi, scheme)


def sort(arr, scheme="hoare", style="iterative"):
    if style == "iterative":
        quicksort_iterative(arr, 0, len(arr) - 1, scheme)
    else:
        quicksort_recursive(arr, 0, len(arr) - 1, scheme)
