from .operations import get_operation
from .calculation import Calculation
from .history import History
from .calculator_memento import CalculatorMemento
from .exceptions import OperationError
from .calculator_config import get_config

class Calculator:
    def __init__(self, history: History | None = None, observers: list | None = None):
        self.config = get_config()
        self.history = history or History(max_size=self.config["max_history"])
        self.observers = observers or []
        self._undo_stack = []
        self._redo_stack = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def _notify(self, calculation):
        for obs in self.observers:
            obs.update(calculation, self.history.to_list())

    def _save_state(self):
        return CalculatorMemento(self.history.to_list())

    def _restore_state(self, memento: CalculatorMemento):
        self.history.clear()
        for c in memento.get_state():
            self.history.add(c)

    def calculate(self, op_name: str, a: float, b: float):
        op = get_operation(op_name)

        self._undo_stack.append(self._save_state())
        self._redo_stack.clear()

        result = op(a, b)
        calc = Calculation(
            op_name,
            a,
            b,
            round(result, self.config["precision"])
        )
        self.history.add(calc)

        self._notify(calc)
        return calc

    def undo(self):
        if not self._undo_stack:
            raise OperationError("Nothing to undo")
        self._redo_stack.append(self._save_state())
        m = self._undo_stack.pop()
        self._restore_state(m)

    def redo(self):
        if not self._redo_stack:
            raise OperationError("Nothing to redo")
        self._undo_stack.append(self._save_state())
        m = self._redo_stack.pop()
        self._restore_state(m)

    def get_history(self):
        return self.history.to_list()
