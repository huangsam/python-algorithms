import pytest

from algorithms.sorting import insertion_sort
from tests.helpers import is_sorted


@pytest.mark.array
@pytest.mark.sorting
def test_insertion_sort(array):
    assert not is_sorted(array)
    insertion_sort.sort(array)
    assert is_sorted(array)
