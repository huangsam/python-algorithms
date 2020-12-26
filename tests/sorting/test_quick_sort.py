import pytest

from algorithms.sorting import quick_sort
from tests.helpers import is_sorted


@pytest.mark.array
@pytest.mark.sorting
def test_quick_sort_iterative(array):
    assert not is_sorted(array)
    quick_sort.sort(array)
    assert is_sorted(array)


@pytest.mark.array
@pytest.mark.sorting
def test_quick_sort_recursive(array):
    assert not is_sorted(array)
    quick_sort.sort(array, iterative=False)
    assert is_sorted(array)
