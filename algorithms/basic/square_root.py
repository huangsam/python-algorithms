def square_root(x, precision=0.05):
    start, end = 1.0, x
    while start < end:
        mid = (start + end) / 2.0
        if mid * mid > x + precision:
            start, end = start, mid
        elif mid * mid < x - precision:
            start, end = mid, end
        else:
            return round(mid, 2)
    return round(start, 2)
