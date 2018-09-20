import pytest

from collection import trie


@pytest.fixture(scope='function')
def simple_trie():
    tr = trie.Trie()
    tr.insert('hello')
    tr.insert('hat')
    tr.insert('cat')
    return tr


class TestTrie(object):

    def test_insert(self):
        tr = trie.Trie()
        tr.insert('hello')
        assert tr.node.is_complete is False
        assert 'h' in tr.node.children
        assert 'e' in tr.node.children['h'].children

    def test_search_found_good(self, simple_trie):
        for word in ('hello', 'cat'):
            found, node = simple_trie.search(word)
            assert found is True
            assert node.ref_count == 1

    def test_search_found_good(self, simple_trie):
        for word in ('he', 'hell', 'ca'):
            found, node = simple_trie.search(word)
            assert found is False
            assert node is not None
            assert node.ref_count == 0

    def test_search_not_found(self, simple_trie):
        found, node = simple_trie.search('fat')
        assert found is False
        assert node is None
