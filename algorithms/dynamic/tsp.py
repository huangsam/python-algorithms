from itertools import permutations


# https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/
def tsp_brute(graph, source):
    other = []
    for i in range(len(graph)):
        if i != source:
            other.append(i)
    min_cost = 2 ** 32 - 1
    for path in permutations(other, len(other)):
        cur_cost = 0
        start = source
        for i in range(len(path)):
            finish = path[i]
            cur_cost += graph[start][finish]
            start = finish
        cur_cost += graph[start][source]
        min_cost = min(min_cost, cur_cost)
    return min_cost
