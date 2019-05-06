import pytest

import algorithms.dynamic.edit_dist as edit


@pytest.mark.string
@pytest.mark.dynamic
class TestEditDist:
    def test_edit_dist_same(self):
        assert edit.edit_dist_rec("abcd", "abcd") == 0

    def test_edit_dist_insert(self):
        assert edit.edit_dist_rec("a", "abcd") == 3

    def test_edit_dist_remove(self):
        assert edit.edit_dist_rec("abcd", "a") == 3

    def test_edit_dist_replace(self):
        assert edit.edit_dist_rec("abcd", "abce") == 1

    @pytest.mark.parametrize(
        "a, b, o",
        [
            ("achoo", "aching", 3),
            ("geek", "gkee", 2),
            ("cat", "cut", 1),
            ("sunday", "saturday", 3),
        ],
    )
    @pytest.mark.parametrize("f", [edit.edit_dist_rec, edit.edit_dist_dp])
    def test_edit_dist_all(self, f, a, b, o):
        assert f(a, b) == o
