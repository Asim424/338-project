from building import Building
from data_structures import Stack

class HistoryEntry:
    def __init__(self, origin: Building, destination: Building, route: Stack, dist: float):
        self.origin = origin
        self.destination = destination
        self.route = route
        self.dist = dist

class History:
    def __init__(self, max_size: int = 50):
        self._stack: list[HistoryEntry] = []
        self.max_size = max_size

    def add(self, origin: Building, destination: Building, route: Stack, dist: float) -> None:
        entry = HistoryEntry(origin, destination, route, dist)
        self._stack.append(entry)
        if len(self._stack) > self.max_size:
            self._stack.pop(0)

    def undo(self) -> HistoryEntry | None:
        if self.is_empty():
            return None
        return self._stack.pop()

    def is_empty(self) -> bool:
        return len(self._stack) == 0

    def peek(self) -> HistoryEntry | None:
        if self.is_empty():
            return None
        return self._stack[-1]