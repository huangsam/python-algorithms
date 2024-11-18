import pytest

from algorithms.array.merge_simple import merge_sort, merge_sorted_arrays


def _is_sorted(array: list[int]) -> bool:
    alen = len(array)
    for i in range(1, alen):
        if array[i - 1] > array[i]:
            return False
    return True


@pytest.mark.array
@pytest.mark.sorting
def test_merge_simple(random_array):
    assert not _is_sorted(random_array)
    random_array = merge_sort(random_array)
    assert _is_sorted(random_array)


@pytest.mark.array
@pytest.mark.sorting
def test_merge_empty():
    assert merge_sort([]) == []


@pytest.mark.array
@pytest.mark.sorting
def test_merge_sorted_array():
    assert merge_sorted_arrays([1, 2, 5, 8, 10], [1, 3, 6, 9, 11]) == [1, 1, 2, 3, 5, 6, 8, 9, 10, 11]
