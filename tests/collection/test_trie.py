from collection import trie


class TestTrie(object):

    def test_insert(self):
        tr = trie.Trie()
        tr.insert('hello')
        assert tr.node.is_complete is False
        assert 'h' in tr.node.children
        assert tr.node.children['h'].is_complete is False
        assert 'e' in tr.node.children['h'].children

    def test_search(self):
        tr = trie.Trie()
        tr.insert('hello')
        tr.insert('hat')
        tr.insert('cat')
        for word in ('he', 'hell', 'cat'):
            found, _ = tr.search('he')
            assert found is True
        found, _ = tr.search('fat')
        assert found is False
