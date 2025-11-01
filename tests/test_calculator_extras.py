import pytest
from app import create_calculator
from app.exceptions import OperationError


def test_undo_without_history():
    calc = create_calculator()
    with pytest.raises(OperationError):
        calc.undo()


def test_redo_without_undo():
    calc = create_calculator()
    with pytest.raises(OperationError):
        calc.redo()
