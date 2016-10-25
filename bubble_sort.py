#!/usr/bin/env python


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


# https://en.wikipedia.org/wiki/Bubble_sort
def bubble_sort(arr):
    alen = len(arr)
    for _ in range(alen):
        for i in range(1, alen):
            if arr[i-1] > arr[i]:
                swap(arr, i-1, i)


def main():
    A = [1, 10, 4, 5, 4, 18, 17, 20, 3, 16]
    print("before:", A)
    bubble_sort(A)
    print("after:", A)

if __name__ == '__main__':
    main()
