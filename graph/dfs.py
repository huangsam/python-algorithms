def dfs(graph, root):
    stack = [root]
    visited = set()
    order = []
    while len(stack) > 0:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for child in graph.get_children(node):
            stack.append(child)
        order.append(node)
    return order
