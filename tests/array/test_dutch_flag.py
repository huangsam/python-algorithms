import pytest

from algorithms.array.dutch_flag import dutch_three, dutch_two


def _verify(result) -> None:
    i = 0
    for j in (0, 1, 2):
        while i < len(result) and result[i] == j:
            i += 1
    assert i == len(result)


@pytest.mark.array
def test_dutch_two_sample():
    arr = [0, 1, 0, 1, 0, 1]
    result = dutch_two(arr)
    _verify(result)


@pytest.mark.array
def test_dutch_two_done():
    arr = [0, 0, 0, 1, 1, 1]
    result = dutch_two(arr)
    _verify(result)


@pytest.mark.array
@pytest.mark.parametrize("n", [0, 1])
def test_dutch_two_all_n(n):
    arr = [n for i in range(6)]
    result = dutch_two(arr)
    _verify(result)


@pytest.mark.array
def test_dutch_three_sample():
    arr = [0, 1, 2, 0, 1, 2]
    result = dutch_three(arr)
    _verify(result)


@pytest.mark.array
def test_dutch_three_done():
    arr = [0, 0, 1, 1, 2, 2]
    result = dutch_three(arr)
    _verify(result)


@pytest.mark.array
@pytest.mark.parametrize("n", [0, 1, 2])
def test_dutch_three_all_n(n):
    arr = [n for i in range(6)]
    result = dutch_three(arr)
    _verify(result)
