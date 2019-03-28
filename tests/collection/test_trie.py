import pytest


@pytest.mark.tree
class TestTrie:
    def test_insert(self, simple_trie):
        assert simple_trie.node.is_complete is False
        assert "h" in simple_trie.node.children
        assert "e" in simple_trie.node.children["h"].children
        simple_trie.insert("happy")
        assert "a" in simple_trie.node.children["h"].children

    @pytest.mark.parametrize("word", ["hello", "hat", "cat"])
    def test_search_found_good(self, simple_trie, word):
        found, node = simple_trie.search(word)
        assert found is True
        assert node is not None
        assert node.ref_count == 1

    @pytest.mark.parametrize("word", ["he", "hell", "ca"])
    def test_search_found_bad(self, simple_trie, word):
        found, node = simple_trie.search(word)
        assert found is False
        assert node is not None
        assert node.ref_count == 0

    @pytest.mark.parametrize("word", ["fat", "car", "road"])
    def test_search_not_found(self, simple_trie, word):
        found, node = simple_trie.search(word)
        assert found is False
        assert node is None
