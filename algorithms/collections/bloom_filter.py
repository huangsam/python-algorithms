import hashlib


class BloomFilter:
    """A space-efficient probabilistic data structure for membership testing."""

    def __init__(self, capacity: int, num_hashes: int):
        self.capacity = capacity
        self.num_hashes = num_hashes
        self.bit_vector = [False] * capacity

    def add(self, item: str):
        """Add an item to the bloom filter."""
        for i in range(self.num_hashes):
            hash_index = self._hash(item, i)
            self.bit_vector[hash_index % self.capacity] = True

    def __contains__(self, item: str) -> bool:
        """Check if an item is likely in the bloom filter."""
        for i in range(self.num_hashes):
            hash_index = self._hash(item, i)
            if not self.bit_vector[hash_index % self.capacity]:
                return False
        return True

    def _hash(self, item: str, seed: int) -> int:
        """Generate a hash for an item with a given seed."""
        # Using hashlib for stable cross-platform hashing
        hash_obj = hashlib.sha256(f"{seed}{item}".encode())
        return int(hash_obj.hexdigest(), 16)
