#!/usr/bin/env python


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


# https://en.wikipedia.org/wiki/Bubble_sort
def sort(arr):
    alen = len(arr)
    while True:
        swapped = False
        for i in range(1, alen):
            if arr[i - 1] > arr[i]:
                swap(arr, i - 1, i)
                swapped = True
        if not swapped:
            break
