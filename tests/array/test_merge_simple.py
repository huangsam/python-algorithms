import pytest

from algorithms.array.merge_simple import merge_sort


def _is_sorted(array):
    alen = len(array)
    for i in range(1, alen):
        if array[i - 1] > array[i]:
            return False
    return True


@pytest.mark.array
@pytest.mark.sorting
def test_merge_simple(array):
    assert not _is_sorted(array)
    array = merge_sort(array)
    assert _is_sorted(array)


@pytest.mark.array
@pytest.mark.sorting
def test_merge_empty():
    arr = []
    actual = merge_sort(arr)
    assert actual == arr
