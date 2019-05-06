# https://www.geeksforgeeks.org/segregate-even-and-odd-numbers/
def even_odd(arr):
    result = [*arr]
    lo = 0
    hi = len(arr) - 1
    while lo < hi:
        while result[lo] % 2 == 0 and lo < hi:
            lo += 1
        while result[hi] % 2 == 1 and lo < hi:
            hi -= 1
        if lo < hi:
            result[lo], result[hi] = result[hi], result[lo]
    return result
