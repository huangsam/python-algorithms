import heapq

from algorithms.collection.tree import TreeNode


def populate(root, mapping, pattern):
    if root is None:
        return
    if root.left is None and root.right is None:
        mapping[root.value] = pattern
    populate(root.left, mapping, pattern + "0")
    populate(root.right, mapping, pattern + "1")


# https://www.techiedelight.com/huffman-coding/
def huffman(frequencies):
    result = {}
    least_queue = []
    for ch, freq in frequencies.items():
        heapq.heappush(least_queue, (freq, TreeNode(ch)))
    while len(least_queue) > 1:
        f_freq, f_node = heapq.heappop(least_queue)
        s_freq, s_node = heapq.heappop(least_queue)
        i_node = TreeNode("*")
        i_node.left = f_node
        i_node.right = s_node
        i_freq = f_freq + s_freq
        heapq.heappush(least_queue, (i_freq, i_node))
    l_freq, l_node = heapq.heappop(least_queue)
    populate(l_node, result, "")
    return result


if __name__ == "__main__":
    result = huffman({"a": 15, "b": 7, "c": 6, "d": 6, "e": 5})
    print(result)
