import pytest

from sorting import quick_sort
from tests.utils import is_sorted


@pytest.mark.array
@pytest.mark.sorting
class TestQuickSort:
    def test_quick_sort_iterative(self, array):
        assert not is_sorted(array)
        quick_sort.sort(array)
        assert is_sorted(array)

    def test_quick_sort_recursive(self, array):
        assert not is_sorted(array)
        quick_sort.sort(array, iterative=False)
        assert is_sorted(array)
