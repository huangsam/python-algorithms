import pytest

from algorithms.sorting import insertion_sort
from tests.helpers import is_sorted


@pytest.mark.array
@pytest.mark.sorting
def test_insertion_sort(random_array):
    assert not is_sorted(random_array)
    insertion_sort.sort(random_array)
    assert is_sorted(random_array)
