# https://en.wikipedia.org/wiki/Bubble_sort
def sort(arr):
    """Sorts the array in place using bubble sort."""
    alen = len(arr)
    while True:
        swapped = False
        for i in range(1, alen):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        if not swapped:
            break
