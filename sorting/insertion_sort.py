# https://en.wikipedia.org/wiki/Insertion_sort
def sort(arr):
    alen = len(arr)
    for i in range(1, alen):
        item = arr[i]
        j = i - 1
        while j >= 0 and item < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item
