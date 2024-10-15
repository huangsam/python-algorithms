# https://www.geeksforgeeks.org/segregate-0s-and-1s-in-an-array-by-traversing-array-once/
def dutch_two(arr: list[int]):
    result = [*arr]
    lo = 0
    hi = len(result) - 1
    while lo <= hi:
        if result[lo] == 0:
            lo += 1
        elif result[lo] == 1:
            result[lo], result[hi] = result[hi], result[lo]
            hi -= 1
    return result


# https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/
# http://users.monash.edu/~lloyd/tildeAlgDS/Sort/Flag/
def dutch_three(arr: list[int]):
    result = [*arr]
    lo = 0
    mid = 0
    hi = len(result) - 1
    while mid <= hi:
        if result[mid] == 0:
            result[lo], result[mid] = result[mid], result[lo]
            lo += 1
            mid += 1
        elif result[mid] == 1:
            mid += 1
        else:
            result[mid], result[hi] = result[hi], result[mid]
            hi -= 1
    return result
