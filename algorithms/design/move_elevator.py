from collections import deque
from enum import Enum, auto
from heapq import heappop, heappush


class Direction(Enum):
    UP = auto()
    DOWN = auto()


class Elevator:
    def __init__(self, current_level: int, requests: set[tuple[int, int]]) -> None:
        self.current_level = current_level
        self.requests = deque(requests)  # Use deque for efficient queue operations
        self.direction = Direction.UP

    def move(self) -> None:
        """Iteratively move the elevator, processing requests in sweeps."""
        while self.requests:
            print(f"== {self.direction.name} from level {self.current_level}")
            bound = self._get_bound()
            priority: list[tuple[int, int]] = []
            visited_requests = set()
            visited_levels = set()

            # Collect valid requests within bound
            for req in list(self.requests):
                if self._spans(bound, req) and self._valid(req):
                    heappush(priority, (self._cost(req[0]), req[0]))
                    heappush(priority, (self._cost(req[1]), req[1]))
                    visited_requests.add(req)

            # Remove processed requests
            self.requests = deque(req for req in self.requests if req not in visited_requests)

            # Visit levels in order of cost
            while priority:
                _, level = heappop(priority)
                if level not in visited_levels:
                    self.current_level = level  # Update position incrementally
                    visited_levels.add(level)
                    print(f"Arrived at level: {level}")

            # If requests remain, switch direction
            if self.requests:
                self.direction = self._opposite(self.direction)

    def _get_bound(self) -> tuple[int, int]:
        """Calculate boundary given remaining operations."""
        if self.direction == Direction.UP:
            max_level = self._get_max_level()
            return self.current_level, max_level
        else:
            min_level = self._get_min_level()
            return min_level, self.current_level

    def _valid(self, req: tuple[int, int]) -> bool:
        """Determine whether request is valid given direction."""
        req_min, req_max = min(req), max(req)
        if self.direction == Direction.UP:
            # Process if we need to go up to reach any part of this request
            return req_max >= self.current_level
        else:
            # Process if we need to go down to reach any part of this request
            return req_min <= self.current_level

    def _cost(self, target) -> int:
        """Determine cost of moving to target."""
        return abs(target - self.current_level)

    def _get_max_level(self) -> int:
        """Get maximum level for remaining requests."""
        return max(v for req in self.requests for v in req)

    def _get_min_level(self) -> int:
        """Get minimum level for remaining requests."""
        return min(v for req in self.requests for v in req)

    def _spans(self, bound: tuple[int, int], req: tuple[int, int]) -> bool:
        """Determine whether boundary spans request."""
        bl, br = bound
        rl, rr = req
        return bl <= rl <= br and bl <= rr <= br

    def _opposite(self, direction) -> Direction:
        """Simple toggle for direction."""
        return Direction.DOWN if direction == Direction.UP else Direction.UP


def main():
    requests = {(4, 8), (7, 4), (6, 3), (8, 9), (1, 2)}
    elevator = Elevator(current_level=5, requests=requests)
    elevator.move()


if __name__ == "__main__":
    main()
