import pytest

from algorithms.sorting import quick_sort
from tests.helpers import is_sorted


@pytest.mark.array
@pytest.mark.sorting
def test_quick_sort_iterative(random_array):
    assert not is_sorted(random_array)
    quick_sort.sort(random_array)
    assert is_sorted(random_array)


@pytest.mark.array
@pytest.mark.sorting
def test_quick_sort_recursive(random_array):
    assert not is_sorted(random_array)
    quick_sort.sort(random_array, iterative=False)
    assert is_sorted(random_array)
