def merge_k(arrays):
    while len(arrays) >= 2:
        arr1 = arrays.pop(0)
        arr2 = arrays.pop(0)
        narr = merge(arr1, arr2)
        arrays.append(narr)
    return arrays.pop(0) if arrays else []


def merge(arr1, arr2):
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
