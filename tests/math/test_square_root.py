import pytest

from algorithms.math.square_root import square_root


@pytest.mark.math
@pytest.mark.parametrize("root, x", [(3.0, 9.0), (6.0, 36.0), (9.0, 81.0), (12.0, 144.0)])
def test_square_root_exact(root, x):
    assert root == square_root(x)


@pytest.mark.math
def test_square_root_exact_tight():
    # Test with tight precision to hit the exact return
    assert 3.0 == square_root(9.0, precision=0.0)


@pytest.mark.math
@pytest.mark.parametrize(
    "left, right, x",
    [
        (2.0, 3.0, 7.0),
        (4.0, 5.0, 18.0),
        (5.0, 6.0, 30.0),
        (11.0, 12.0, 130.0),
        (14.0, 15.0, 200.0),
    ],
)
def test_square_root_about(left: float, right: float, x: float):
    assert left < square_root(x) < right
