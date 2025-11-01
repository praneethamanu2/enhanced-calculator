import pytest
from app.operations import get_operation
from app.exceptions import OperationError


def test_root_zero_root_error():
    op = get_operation("root")
    with pytest.raises(OperationError):
        op(4, 0)


def test_root_even_root_of_negative_error():
    op = get_operation("root")
    with pytest.raises(OperationError):
        op(-8, 2)


def test_modulus_by_zero_error():
    op = get_operation("modulus")
    with pytest.raises(OperationError):
        op(5, 0)


def test_int_divide_by_zero_error():
    op = get_operation("int_divide")
    with pytest.raises(OperationError):
        op(10, 0)


def test_percent_zero_base_error():
    op = get_operation("percent")
    with pytest.raises(OperationError):
        op(5, 0)


def test_get_operation_invalid_name():
    """Covers invalid operation branch in get_operation()."""
    with pytest.raises(OperationError):
        get_operation("not_a_real_operation")
