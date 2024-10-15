import heapq


def merge_k_split(arrays: list[list[int]]):
    if len(arrays) == 0:
        return []
    if len(arrays) == 1:
        return arrays[0]
    if len(arrays) == 2:
        return merge_two_arrays(arrays[0], arrays[1])
    mid = len(arrays) // 2
    left_merge = merge_k_split(arrays[:mid])
    right_merge = merge_k_split(arrays[mid:])
    return merge_two_arrays(left_merge, right_merge)


def merge_two_arrays(arr1: list[int], arr2: list[int]):
    i1 = 0
    i2 = 0
    result = []
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] < arr2[i2]:
            result.append(arr1[i1])
            i1 += 1
        else:
            result.append(arr2[i2])
            i2 += 1
    if i1 >= len(arr1):
        result.extend(arr2[i2:])
    elif i2 >= len(arr2):
        result.extend(arr1[i1:])
    return result


# https://www.geeksforgeeks.org/merge-k-sorted-arrays/
def merge_k_heap(arrays: list[list[int]]):
    result = []

    heap = [(arr[0], i, 0) for i, arr in enumerate(arrays) if arr]
    heapq.heapify(heap)

    while heap:
        val, arr_ind, element_ind = heapq.heappop(heap)

        result.append(val)

        if element_ind + 1 < len(arrays[arr_ind]):
            next_tuple = (arrays[arr_ind][element_ind + 1], arr_ind, element_ind + 1)
            heapq.heappush(heap, next_tuple)
    return result
