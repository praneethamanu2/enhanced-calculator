from collections import deque
from .calculation import Calculation

class History:
    def __init__(self, max_size=100):
        self._entries = deque(maxlen=max_size)

    def add(self, calc: Calculation):
        self._entries.append(calc)

    def clear(self):
        self._entries.clear()

    def to_list(self):
        return list(self._entries)

    def __iter__(self):
        return iter(self._entries)
