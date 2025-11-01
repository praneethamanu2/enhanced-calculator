import pytest
from app import create_calculator
from app.exceptions import OperationError

def test_calculator_add_and_history():
    calc = create_calculator()
    calc.calculate("add", 2, 3)
    history = calc.get_history()
    assert len(history) == 1
    assert history[0].result == 5

def test_undo_redo():
    calc = create_calculator()
    calc.calculate("add", 2, 3)
    calc.undo()
    assert len(calc.get_history()) == 0
    calc.redo()
    assert len(calc.get_history()) == 1

def test_redo_without_undo_fails():
    calc = create_calculator()
    with pytest.raises(OperationError):
        calc.redo()
