import pytest

from algorithms.sorting import bubble_sort
from tests.utils import is_sorted


@pytest.mark.array
@pytest.mark.sorting
class TestBubbleSort:
    def test_bubble_sort(self, array):
        assert not is_sorted(array)
        bubble_sort.sort(array)
        assert is_sorted(array)
