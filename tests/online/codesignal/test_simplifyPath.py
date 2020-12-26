import pytest

from algorithms.online.codesignal.simplifyPath import simplifyPath


@pytest.mark.string
@pytest.mark.parametrize(
    "long_path, short_path",
    [
        ("/x/./y/./z/..//a", "/x/y/a"),
        ("/home/a/./x/../b//c/", "/home/a/b/c"),
        ("/a/b/c/../..", "/a"),
        ("/../", "/"),
        ("/.././///", "/"),
        ("a/b/../c/d/../../e/../../a/", "/a"),
    ],
)
def test_simplify(long_path, short_path):
    assert simplifyPath(long_path) == short_path
