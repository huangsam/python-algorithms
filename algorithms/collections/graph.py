from collections import defaultdict


class Graph:
    """Graph stored as adjacency list."""

    def __init__(self, *edges):
        self.nodes = set()
        self.graph = defaultdict(set)
        self.ingress = defaultdict(int)
        for src, dst in edges:
            self.add_edge(src, dst)
            self.add_nodes(src, dst)

    def add_nodes(self, *nodes):
        for node in nodes:
            self.nodes.add(node)

    def add_edge(self, src, dst):
        raise NotImplementedError

    def get_children(self, src):
        return sorted(self.graph[src])

    def get_nodes(self):
        return self.nodes

    def get_out_degree(self, src):
        return len(self.graph[src])

    def get_in_degree(self, src):
        return self.ingress[src]

    def check_node(self, src):
        return src in self.nodes

    def check_edge(self, pair):
        src, dst = pair
        return dst in self.graph[src]


class DirectedGraph(Graph):
    """Directed graph."""

    def add_edge(self, src, dst):
        if dst in self.graph[src]:
            raise ValueError(f"edge from {src} to {dst} already exists")
        self.graph[src].add(dst)
        self.ingress[dst] += 1
        self.add_nodes(src, dst)


class UndirectedGraph(Graph):
    """Undirected graph."""

    def add_edge(self, src, dst):
        if dst in self.graph[src]:
            raise ValueError(f"edge from {src} to {dst} already exists")
        self.graph[src].add(dst)
        self.graph[dst].add(src)
        self.ingress[src] += 1
        self.ingress[dst] += 1
        self.add_nodes(src, dst)
