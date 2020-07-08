from algorithms.collection.graph import Graph


def dfs(graph: Graph, root):
    stack = [root]
    visited = set()
    scanned = []
    while len(stack) > 0:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for child in graph.get_children(node):
            if child in visited:
                continue
            stack.append(child)
        scanned.append(node)
    return scanned
