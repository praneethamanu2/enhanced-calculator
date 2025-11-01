import pytest
from app.operations import get_operation
from app.exceptions import OperationError

@pytest.mark.parametrize("name,a,b,expected", [
    ("add", 2, 3, 5),
    ("subtract", 5, 3, 2),
    ("multiply", 2, 4, 8),
    ("divide", 8, 2, 4),
    ("power", 2, 3, 8),
    ("modulus", 5, 2, 1),
    ("int_divide", 5, 2, 2),
    ("percent", 50, 100, 50),
    ("abs_diff", 5, 9, 4),
])
def test_operations(name, a, b, expected):
    op = get_operation(name)
    assert op(a, b) == expected

def test_divide_by_zero():
    op = get_operation("divide")
    with pytest.raises(OperationError):
        op(1, 0)

def test_modulus_by_zero():
    op = get_operation("modulus")
    with pytest.raises(OperationError):
        op(5, 0)


def test_int_divide_by_zero():
    op = get_operation("int_divide")
    with pytest.raises(OperationError):
        op(5, 0)


def test_root_errors():
    op = get_operation("root")
    # Zero root is invalid
    with pytest.raises(OperationError):
        op(4, 0)
    # Even root of negative number is invalid
    with pytest.raises(OperationError):
        op(-8, 2)