from collections import defaultdict


class Graph:
    """Helper for managing dictionary-based graph."""

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
        self.graph[src].add(dst)
        self.ingress[dst] += 1
        self.add_nodes(src, dst)

    def get_children(self, src):
        return sorted(self.graph[src])

    def get_nodes(self):
        return self.nodes

    def get_out_degree(self, src):
        return len(self.graph[src])

    def get_in_degree(self, src):
        return self.ingress[src]
