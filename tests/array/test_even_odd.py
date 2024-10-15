import pytest

from algorithms.array import even_odd as seg


def _verify(arr: list[int]):
    lo = 0
    hi = len(arr) - 1
    while arr[lo] % 2 == 0 and lo < hi:
        if arr[lo + 1] % 2 == 1:
            break
        lo += 1
    while arr[hi] % 2 == 1 and lo < hi:
        if arr[hi - 1] % 2 == 0:
            break
        hi -= 1
    assert 0 <= hi - lo <= 1


@pytest.mark.math
@pytest.mark.array
def test_even_odd_sample():
    arr = [12, 34, 45, 9, 8, 90, 3]
    result = seg.even_odd(arr)
    _verify(result)


@pytest.mark.math
@pytest.mark.array
def test_even_odd_zigzag():
    arr = [1, 2, 3, 4, 5, 6]
    result = seg.even_odd(arr)
    _verify(result)


@pytest.mark.math
@pytest.mark.array
def test_even_odd_done():
    arr = [2, 4, 1, 3]
    result = seg.even_odd(arr)
    _verify(result)


@pytest.mark.math
@pytest.mark.array
def test_even_odd_done_all_odd():
    arr = [1, 3, 5, 7]
    result = seg.even_odd(arr)
    _verify(result)


@pytest.mark.math
@pytest.mark.array
def test_even_odd_done_all_even():
    arr = [2, 4, 6, 8]
    result = seg.even_odd(arr)
    _verify(result)
