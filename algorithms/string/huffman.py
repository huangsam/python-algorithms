import heapq

from algorithms.collections.tree import TreeNode


def populate(root, mapping, pattern):
    if root is None:
        return
    if root.left is None and root.right is None:
        mapping[root.value] = pattern
    populate(root.left, mapping, pattern + "0")
    populate(root.right, mapping, pattern + "1")


# https://www.techiedelight.com/huffman-coding/
# https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/
def huffman(frequencies):
    result = {}
    least_queue = []
    for ch, freq in frequencies.items():
        heapq.heappush(least_queue, (freq, TreeNode(ch)))
    while len(least_queue) > 1:
        l_freq, l_node = heapq.heappop(least_queue)
        r_freq, r_node = heapq.heappop(least_queue)
        i_node = TreeNode("*")
        i_node.left = l_node
        i_node.right = r_node
        i_freq = l_freq + r_freq
        heapq.heappush(least_queue, (i_freq, i_node))
    l_freq, l_node = heapq.heappop(least_queue)
    populate(l_node, result, "")
    return result
