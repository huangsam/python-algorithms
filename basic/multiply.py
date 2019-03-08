# https://www.geeksforgeeks.org/russian-peasant-multiply-two-numbers-using-bitwise-operators/
def multiply(x, y):
    if x < 0:
        raise ValueError("x is a negative number")
    elif y < 0:
        raise ValueError("y is a negative number")
    out = 0
    while y > 0:
        if y & 1 == 1:
            out += x
        x = x << 1
        y = y >> 1
    return out
