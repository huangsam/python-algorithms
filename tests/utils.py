def is_sorted(array):
    alen = len(array)
    for i in range(1, alen):
        if array[i - 1] > array[i]:
            return False
    return True
