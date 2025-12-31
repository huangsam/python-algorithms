import pytest

from algorithms.online.codesignal.kthLargestElement import kthLargestElement


@pytest.mark.online
def test_kthLargestElement():
    assert kthLargestElement([3, 1, 4, 1, 5], 2) == 4
    assert kthLargestElement([1, 2, 3, 4, 5], 1) == 5
