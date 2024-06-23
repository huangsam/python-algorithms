from itertools import permutations

from algorithms.constants import MAX_INT


# https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/
def tsp_brute(graph: list[list[int]], source: int):
    other = []
    for i in range(len(graph)):
        if i != source:
            other.append(i)
    min_cost = MAX_INT
    for path in permutations(other, len(other)):
        cur_cost = 0
        sv = source
        for tv in path:
            cur_cost += graph[sv][tv]
            sv = tv
        cur_cost += graph[sv][source]
        min_cost = min(min_cost, cur_cost)
    return min_cost
