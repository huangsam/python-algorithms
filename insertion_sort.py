#!/usr/bin/env python


# https://en.wikipedia.org/wiki/Insertion_sort
def insertion_sort(arr):
    alen = len(arr)
    for i, ival in enumerate(arr):
        item = ival
        j = i-1
        while j >= 0 and item < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = item


def main():
    A = [1, 10, 4, 5, 4, 18, 17, 20, 3, 16]
    print("before:", A)
    insertion_sort(A)
    print("after:", A)

if __name__ == '__main__':
    main()
