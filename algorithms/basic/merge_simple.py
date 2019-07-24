def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    l_merged = merge_sort(arr[:middle])
    r_merged = merge_sort(arr[middle:])
    return merge_arrays(l_merged, r_merged)


def merge_arrays(arr1, arr2):
    result = []
    a1, a2 = 0, 0
    while a1 < len(arr1) and a2 < len(arr2):
        if arr1[a1] < arr2[a2]:
            result.append(arr1[a1])
            a1 += 1
        else:
            result.append(arr2[a2])
            a2 += 1
    if arr1:
        return result + arr1[a1:]
    return result + arr2[a2:]
