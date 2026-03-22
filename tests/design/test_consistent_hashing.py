import pytest

from algorithms.design.consistent_hashing import ConsistentHashing


@pytest.mark.design
def test_consistent_hashing_assignment():
    nodes = ["A", "B"]
    ch = ConsistentHashing(nodes)
    node1 = ch.get_node("key1")
    assert node1 in nodes


@pytest.mark.design
def test_consistent_hashing_consistency():
    ch = ConsistentHashing(["A", "B", "C"])
    key = "persistent_key"
    first_node = ch.get_node(key)
    # Should always map to same node if nodes don't change
    for _ in range(10):
        assert ch.get_node(key) == first_node


@pytest.mark.design
def test_consistent_hashing_redistribution():
    ch = ConsistentHashing(["A", "B"])
    key = "some_key"
    old_node = ch.get_node(key)

    ch.add_node("C")
    # key might or might not move, but it shouldn't error
    assert ch.get_node(key) in ["A", "B", "C"]

    ch.remove_node(old_node)
    assert ch.get_node(key) != old_node
