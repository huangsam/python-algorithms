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
    while True:
        if a1 >= len(arr1):
            result.extend(arr2[a2:])
            break
        elif a2 >= len(arr2):
            result.extend(arr1[a1:])
            break
        else:
            if arr1[a1] <= arr2[a2]:
                result.append(arr1[a1])
                a1 += 1
            else:
                result.append(arr2[a2])
                a2 += 1
    return result
