# https://www.geeksforgeeks.org/rotate-bits-of-an-integer/
def rotate_bits(x, d):
    bits = 16
    mask = 2 ** bits - 1
    rotate = d % bits
    left = x << rotate
    right = x >> (bits - rotate)
    return bin(mask & (left | right))
