class Node:
    """A set of trie children exist down the line."""

    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.is_complete = False
        self.ref_count = 0


# https://jamesroutley.co.uk/tech/2017/07/16/tries.html#implementation
class Trie:
    """Trie tree starts with a root character."""

    def __init__(self):
        self.node = Node()

    def insert(self, key: str):
        node = self.node
        for letter in key:
            if letter in node.children:
                node = node.children[letter]
            else:
                new_node = Node(letter)
                node.children[letter] = new_node
                node = new_node
        node.is_complete = True

    # Optimized to account for rework
    def search(self, key: str, prev_node: Node | None = None):
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
