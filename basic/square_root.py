def square_root(x, error=0.05):
    """Square root of x.

    Args:
        x: The input to compute the square root of.
        error: The margin of acceptible error.

    Returns:
        The output estimated within two decimal places.
    """
    start, end = 1.0, x
    while start < end:
        mid = (start + end) / 2.0
        if mid * mid > x + error:
            start, end = start, mid
        elif mid * mid < x - error:
            start, end = mid, end
        else:
            return round(mid, 2)
    return round(start, 2)
