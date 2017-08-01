def square_root(x, error=0.05):
    """Square root of x.

    Args:
        x (int/float): The input to compute the square root of.

    Returns:
        float: The output estimated within two decimal places.
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


def main():
    assert 9.0 == square_root(81)
    assert 12.0 == square_root(144)
    assert 13.0 == square_root(169)
    assert 14.0 < square_root(200) and \
        square_root(200) < 15.0


if __name__ == '__main__':
    main()
