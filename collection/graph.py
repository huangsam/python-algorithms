class Graph(object):
    """Helper for managing dictionary-based graph."""

    def __init__(self, *edges):
        self.nodes = set()
        self.graph = {}
        for src, dst in edges:
            self.add_edge(src, dst)
            self._add_nodes(src, dst)

    def _add_nodes(self, *nodes):
        for node in nodes:
            self.nodes.add(node)

    def add_edge(self, src, dst):
        if src not in self.graph:
            self.graph[src] = set()
        self.graph[src].add(dst)
        self._add_nodes(src, dst)

    def get_children(self, a):
        return self.graph.get(a)

    def get_nodes(self):
        return self.nodes
