def bfs(graph, root):
    queue = [root]
    visited = set()
    scanned = []
    while len(queue) > 0:
        node = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        for child in graph.get_children(node):
            queue.append(child)
        scanned.append(node)
    return scanned