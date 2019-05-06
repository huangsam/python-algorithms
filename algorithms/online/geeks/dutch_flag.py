# https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/
# http://users.monash.edu/~lloyd/tildeAlgDS/Sort/Flag/
def dutch_flag(arr):
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
