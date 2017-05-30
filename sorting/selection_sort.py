#!/usr/bin/env python


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


# https://en.wikipedia.org/wiki/Selection_sort
def sort(arr):
    alen = len(arr)
    for sort_index in range(0, alen):
        min_index = sort_index
        for i in range(sort_index, alen):
            if arr[i] < arr[min_index]:
                min_index = i
        swap(arr, sort_index, min_index)
