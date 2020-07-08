from typing import List

from algorithms.collection.trie import Trie


# https://www.geeksforgeeks.org/auto-complete-feature-using-trie/
def autocomplete(s: str, queries: List[str]):
    trie = Trie()
    for query in queries:
        trie.insert(query)
    is_word, node = trie.search(s)
    if node is None:
        return []
    result = []
    to_visit = [(node, s)]
    while len(to_visit) > 0:
        cur_node, cur_str = to_visit.pop(0)
        if cur_node.is_complete is True:
            result.append(cur_str)
        for child in cur_node.children.values():
            to_visit.append((child, cur_str + child.value))
    return result
