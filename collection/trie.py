# https://jamesroutley.co.uk/tech/2017/07/16/tries.html#implementation
class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.is_complete = False


class Trie(object):
    def __init__(self):
        self.node = Node()

    def insert(self, key):
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
    def search(self, key, prev_node=None):
        node = prev_node if prev_node is not None else self.node
        for letter in key:
            if letter not in node.children:
                return False
            else:
                node = node.children[letter]
        return True, node
