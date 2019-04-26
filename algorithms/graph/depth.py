def dfs(graph, root):
    stack = [root]
    visited = set()
    scanned = []
    while len(stack) > 0:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for child in graph.get_children(node):
            stack.append(child)
        scanned.append(node)
    return scanned
