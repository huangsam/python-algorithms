#!/usr/bin/env python


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


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


def partition_iterative(arr, lo, hi, stack):
    p = lomuto(arr, lo, hi)
    stack.append((lo, p - 1))
    stack.append((p + 1, hi))


def partition_recursive(arr, lo, hi):
    p = lomuto(arr, lo, hi)
    quicksort_recursive(arr, lo, p - 1)
    quicksort_recursive(arr, p + 1, hi)


def quicksort_iterative(arr, lo, hi):
    stack = [(lo, hi)]
    while len(stack) > 0:
        lo, hi = stack.pop()
        if lo < hi:
            partition_iterative(arr, lo, hi, stack)


def quicksort_recursive(arr, lo, hi):
    if lo < hi:
        partition_recursive(arr, lo, hi)


def sort(arr, iterative=True):
    if iterative is True:
        quicksort_iterative(arr, 0, len(arr) - 1)
    else:
        quicksort_recursive(arr, 0, len(arr) - 1)
