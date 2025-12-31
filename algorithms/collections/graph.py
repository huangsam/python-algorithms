from abc import ABC, abstractmethod
from collections import defaultdict


class Graph(ABC):
    """Graph stored as adjacency list."""

    def __init__(self, *edges: tuple):
        """Initializes the graph with optional edges."""
        self.nodes: set = set()
        self.graph: defaultdict = defaultdict(set)
        self.ingress: defaultdict = defaultdict(int)
        for src, dst in edges:
            self.add_edge(src, dst)
            self.nodes.update([src, dst])

    @abstractmethod
    def add_edge(self, src, dst) -> None:
        """Adds an edge from src to dst."""
        raise NotImplementedError

    def get_children(self, src) -> list:
        """Returns the sorted list of children (neighbors) for the given node."""
        return sorted(self.graph[src])

    def get_nodes(self) -> set:
        """Returns the set of all nodes in the graph."""
        return self.nodes

    def get_out_degree(self, src) -> int:
        """Returns the out-degree of the given node."""
        return len(self.graph[src])

    def get_in_degree(self, src) -> int:
        """Returns the in-degree of the given node."""
        return self.ingress[src]

    def check_node(self, src) -> bool:
        """Checks if the node exists in the graph."""
        return src in self.nodes

    def check_edge(self, src, dst) -> bool:
        """Checks if there is an edge from src to dst."""
        return dst in self.graph[src]


class DirectedGraph(Graph):
    """Directed graph."""

    def add_edge(self, src, dst):
        """Adds a directed edge from src to dst."""
        if dst in self.graph[src]:
            raise ValueError(f"edge from {src} to {dst} already exists")
        self.graph[src].add(dst)
        self.ingress[dst] += 1
        self.nodes.update([src, dst])


class UndirectedGraph(Graph):
    """Undirected graph."""

    def add_edge(self, src, dst):
        """Adds an undirected edge between src and dst."""
        if dst in self.graph[src]:
            raise ValueError(f"edge from {src} to {dst} already exists")
        self.graph[src].add(dst)
        self.graph[dst].add(src)
        self.ingress[src] += 1
        self.ingress[dst] += 1
        self.nodes.update([src, dst])
