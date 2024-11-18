import pytest

from algorithms.sorting import bubble_sort
from tests.helpers import is_sorted


@pytest.mark.array
@pytest.mark.sorting
def test_bubble_sort(random_array):
    assert not is_sorted(random_array)
    bubble_sort.sort(random_array)
    assert is_sorted(random_array)
