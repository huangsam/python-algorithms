# https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
def floyd_warshall(graph: list[list[int]]):
    V = len(graph)
    dist = [i[:] for i in graph]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


# https://www.geeksforgeeks.org/transitive-closure-of-a-graph/
def transitive_closure(graph: list[list[int]]):
    V = len(graph)
    reach = [i[:] for i in graph]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    return reach
