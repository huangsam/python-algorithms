class TrieNode:
    """A set of trie children exist down the line.

    A node in a trie (prefix tree) data structure, containing a value, a dictionary of children nodes,
    and flags for word completion and reference counting. Tries are efficient for storing and searching
    strings with common prefixes, reducing space for shared prefixes.
    """

    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.is_complete = False
        self.ref_count = 0


# https://jamesroutley.co.uk/tech/2017/07/16/tries.html#implementation
class Trie:
    """Trie tree starts with a root character.

    A trie data structure for efficient string storage and retrieval. It uses a tree where each node
    represents a character, allowing for fast prefix searches, insertions, and lookups. This implementation
    supports reference counting for optimization in scenarios with repeated strings.
    """

    def __init__(self):
        self.node = TrieNode()

    def insert(self, key: str):
        """Inserts a key into the trie."""
        node = self.node
        for letter in key:
            if letter in node.children:
                node = node.children[letter]
            else:
                new_node = TrieNode(letter)
                node.children[letter] = new_node
                node = new_node
        node.is_complete = True

    # Optimized to account for rework
    def search(self, key: str, prev_node: TrieNode | None = None) -> tuple[bool, TrieNode | None]:
        """Searches for a key in the trie, returning if found and the node."""
        node = prev_node if prev_node is not None else self.node
        for letter in key:
            if letter not in node.children:
                return False, None
            else:
                node = node.children[letter]
        if node.is_complete:
            node.ref_count += 1
            return True, node
        else:
            return False, node
