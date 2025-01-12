def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left_merged = merge_sort(arr[:middle])
    right_merged = merge_sort(arr[middle:])
    return merge_sorted_arrays(left_merged, right_merged)


def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    result = []
    a1, a2 = 0, 0
    while a1 < len(arr1) and a2 < len(arr2):
        if arr1[a1] < arr2[a2]:
            result.append(arr1[a1])
            a1 += 1
        else:
            result.append(arr2[a2])
            a2 += 1
    return result + arr1[a1:] + arr2[a2:]
