from copy import deepcopy

class CalculatorMemento:
    def __init__(self, state):
        self._state = deepcopy(state)

    def get_state(self):
        return deepcopy(self._state)
