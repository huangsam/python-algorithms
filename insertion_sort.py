#!/usr/bin/env python


# https://en.wikipedia.org/wiki/Insertion_sort
def sort(arr):
    for i, ival in enumerate(arr):
        item = ival
        j = i - 1
        while j >= 0 and item < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item
