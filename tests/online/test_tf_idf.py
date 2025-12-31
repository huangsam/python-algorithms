import pytest

from algorithms.online.tf_idf import tf_idf


@pytest.mark.online
def test_tf_idf():
    docs = {
        0: ["hello world", "world peace"],
        1: ["hello moon", "moon light"],
    }
    result = tf_idf(docs, 0, "hello")
    assert result == 0.0  # appears in both docs, idf=0
    result_world = tf_idf(docs, 0, "world")
    assert result_world > 0  # appears in doc 0 only
