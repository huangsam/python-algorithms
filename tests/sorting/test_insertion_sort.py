import pytest

from algorithms.sorting import insertion_sort
from tests.utils import is_sorted


@pytest.mark.array
@pytest.mark.sorting
class TestInsertionSort:
    def test_insertion_sort(self, array):
        assert not is_sorted(array)
        insertion_sort.sort(array)
        assert is_sorted(array)
