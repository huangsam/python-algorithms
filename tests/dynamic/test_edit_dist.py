import pytest

from algorithms.dynamic import edit_dist as edit


@pytest.mark.string
@pytest.mark.dynamic
@pytest.mark.parametrize(
    "a, b, o",
    [
        ("", "", 0),
        ("abcd", "abcd", 0),
        ("a", "abc", 2),
        ("abc", "a", 2),
        ("cat", "cut", 1),
        ("geek", "gkee", 2),
        ("achoo", "aching", 3),
        ("sunday", "saturday", 3),
    ],
)
@pytest.mark.parametrize("f", [edit.edit_dist_rec, edit.edit_dist_dp])
def test_edit_dist(f, a, b, o):
    assert f(a, b) == o
