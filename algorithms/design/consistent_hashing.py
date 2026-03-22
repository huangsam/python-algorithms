import bisect
import hashlib


class ConsistentHashing:
    """A consistent hashing implementation with virtual nodes."""

    def __init__(self, nodes: list[str] | None = None, virtual_nodes: int = 100):
        self.virtual_nodes_count = virtual_nodes
        self.ring: list[int] = []
        self.node_map: dict[int, str] = {}
        if nodes:
            for node in nodes:
                self.add_node(node)

    def add_node(self, node: str):
        """Add a node to the ring with its virtual nodes."""
        for i in range(self.virtual_nodes_count):
            node_hash = self._hash(f"{node}:{i}")
            self.node_map[node_hash] = node
            bisect.insort(self.ring, node_hash)

    def remove_node(self, node: str):
        """Remove a node and all its virtual nodes from the ring."""
        for i in range(self.virtual_nodes_count):
            node_hash = self._hash(f"{node}:{i}")
            del self.node_map[node_hash]
            ring_index = bisect.bisect_left(self.ring, node_hash)
            self.ring.pop(ring_index)

    def get_node(self, key: str) -> str | None:
        """Get the node responsible for the given key."""
        if not self.ring:
            return None
        item_hash = self._hash(key)
        ring_index = bisect.bisect_left(self.ring, item_hash)
        if ring_index == len(self.ring):
            ring_index = 0
        return self.node_map[self.ring[ring_index]]

    def _hash(self, key: str) -> int:
        """Generate a stable hash for a key."""
        return int(hashlib.md5(key.encode()).hexdigest(), 16)


def main():
    nodes = ["Node-A", "Node-B", "Node-C"]
    ch = ConsistentHashing(nodes)

    keys = ["user1", "user2", "user3", "user4", "user5"]
    for key in keys:
        print(f"Key '{key}' maps to '{ch.get_node(key)}'")

    print("\nRemoving Node-B...")
    ch.remove_node("Node-B")
    for key in keys:
        print(f"Key '{key}' maps to '{ch.get_node(key)}'")
