import pytest

from algorithms.string.myers_diff import myers_diff


@pytest.mark.string
def test_myers_diff_simple():
    src = "ABC"
    dst = "ACB"
    script = myers_diff(src, dst)
    # A B C -> A C B: delete B (pos 1), insert C (pos 1), keep A, keep C, delete original C
    # Wait, Myers finds MINIMAL edit sequence.
    # ABC -> ACB: keep A, delete B, keep C, insert B (if we use B)
    # Or keep A, insert C, keep B, delete C.

    # Constructing result from script
    result = []
    for tag, item in script:
        if tag in ("keep", "insert"):
            result.append(item)
    assert "".join(result) == dst


@pytest.mark.string
def test_myers_diff_identity():
    src = "ABC"
    script = myers_diff(src, src)
    assert all(tag == "keep" for tag, _ in script)
    assert "".join(item for _, item in script) == src


@pytest.mark.string
def test_myers_diff_empty():
    assert myers_diff("", "") == []
    assert myers_diff("", "abc") == [("insert", "a"), ("insert", "b"), ("insert", "c")]
