# https://www.geeksforgeeks.org/a-product-array-puzzle/
def product_array(arr):
    l_mult, r_mult = 1, 1
    new_arr = [1] * len(arr)
    i = 1
    while i < len(arr):
        l_mult *= arr[i-1]
        new_arr[i] *= l_mult
        r_mult *= arr[len(arr)-i]
        new_arr[len(arr)-i-1] *= r_mult
        i += 1
    return new_arr
