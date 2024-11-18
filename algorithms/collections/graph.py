from abc import ABC, abstractmethod
from collections import defaultdict


class Graph(ABC):
    """Graph stored as adjacency list."""

    def __init__(self, *edges):
        self.nodes = set()
        self.graph = defaultdict(set)
        self.ingress = defaultdict(int)
        for src, dst in edges:
            self.add_edge(src, dst)
            self.nodes.update([src, dst])

    @abstractmethod
    def add_edge(self, src, dst) -> None:
        raise NotImplementedError

    def get_children(self, src) -> list:
        return sorted(self.graph[src])

    def get_nodes(self) -> set:
        return self.nodes

    def get_out_degree(self, src) -> int:
        return len(self.graph[src])

    def get_in_degree(self, src) -> int:
        return self.ingress[src]

    def check_node(self, src) -> bool:
        return src in self.nodes

    def check_edge(self, src, dst) -> bool:
        return dst in self.graph[src]


class DirectedGraph(Graph):
    """Directed graph."""

    def add_edge(self, src, dst):
        if dst in self.graph[src]:
            raise ValueError(f"edge from {src} to {dst} already exists")
        self.graph[src].add(dst)
        self.ingress[dst] += 1
        self.nodes.update([src, dst])


class UndirectedGraph(Graph):
    """Undirected graph."""

    def add_edge(self, src, dst):
        if dst in self.graph[src]:
            raise ValueError(f"edge from {src} to {dst} already exists")
        self.graph[src].add(dst)
        self.graph[dst].add(src)
        self.ingress[src] += 1
        self.ingress[dst] += 1
        self.nodes.update([src, dst])
