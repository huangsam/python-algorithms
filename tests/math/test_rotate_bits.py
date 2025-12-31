import pytest

from algorithms.math.rotate_bits import rotate_bits


@pytest.mark.math
def test_rotate_bits():
    # Test basic rotation
    result = rotate_bits(0b1010, 1)
    # Should be binary string
    assert isinstance(result, str)
    assert result.startswith("0b")
