def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


def copy_array(a, begin, end, b):
    for k in range(begin, end):
        b[k] = a[k]
