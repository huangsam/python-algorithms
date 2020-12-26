import pytest

from algorithms.array import dutch_flag as dutch


def _verify(arr):
    i = 0
    for j in (0, 1, 2):
        while i < len(arr) and arr[i] == j:
            i += 1
    assert i == len(arr)


@pytest.mark.array
def test_dutch_two_sample():
    arr = [0, 1, 0, 1, 0, 1]
    result = dutch.dutch_two(arr)
    _verify(result)


@pytest.mark.array
def test_dutch_two_done():
    arr = [0, 0, 0, 1, 1, 1]
    result = dutch.dutch_two(arr)
    _verify(result)


@pytest.mark.array
@pytest.mark.parametrize("n", [0, 1])
def test_dutch_two_all_n(n):
    arr = [n for i in range(6)]
    result = dutch.dutch_two(arr)
    _verify(result)


@pytest.mark.array
def test_dutch_three_sample():
    arr = [0, 1, 2, 0, 1, 2]
    result = dutch.dutch_three(arr)
    _verify(result)


@pytest.mark.array
def test_dutch_three_done():
    arr = [0, 0, 1, 1, 2, 2]
    result = dutch.dutch_three(arr)
    _verify(result)


@pytest.mark.array
@pytest.mark.parametrize("n", [0, 1, 2])
def test_dutch_three_all_n(n):
    arr = [n for i in range(6)]
    result = dutch.dutch_three(arr)
    _verify(result)
