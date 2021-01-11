# https://www.geeksforgeeks.org/a-product-array-puzzle/
def product_array(arr):
    l_multi, r_multi = 1, 1
    new_arr = [1] * len(arr)
    for i in range(1, len(arr)):
        l_multi *= arr[i - 1]
        new_arr[i] *= l_multi
        r_multi *= arr[len(arr) - i]
        new_arr[len(arr) - i - 1] *= r_multi
    return new_arr
