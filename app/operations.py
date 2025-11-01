"""
operations.py
-------------
Defines all arithmetic operations supported by the Enhanced Calculator.
Implements the Factory Design Pattern via the `get_operation()` function
to return operation functions dynamically.
"""

from .exceptions import OperationError


# -------------------------------
# Basic arithmetic operations
# -------------------------------

def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference (a - b)."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient (a / b). Raise error if b == 0."""
    if b == 0:
        raise OperationError("Division by zero")
    return a / b


# -------------------------------
# Advanced arithmetic operations
# -------------------------------

def power(a: float, b: float) -> float:
    """Return a raised to the power of b."""
    return a ** b


def root(a: float, b: float) -> float:
    """
    Return the b-th root of a.
    Raises OperationError if:
        - b == 0 (zero root)
        - a is negative and b is even (no real root)
    """
    if b == 0:
        raise OperationError("Zero root is undefined")
    if a < 0 and b % 2 == 0:
        raise OperationError("Even root of a negative number is not real")
    return a ** (1 / b)


def modulus(a: float, b: float) -> float:
    """Return a % b. Raise error if b == 0."""
    if b == 0:
        raise OperationError("Modulus by zero")
    return a % b


def int_divide(a: float, b: float) -> int:
    """Return integer division result of a // b. Raise error if b == 0."""
    if b == 0:
        raise OperationError("Integer division by zero")
    return a // b


def percent(a: float, b: float) -> float:
    """Return (a / b) * 100. Raise error if b == 0."""
    if b == 0:
        raise OperationError("Percentage of zero base is undefined")
    return (a / b) * 100


def abs_diff(a: float, b: float) -> float:
    """Return the absolute difference between a and b."""
    return abs(a - b)


# -------------------------------
# Factory design pattern
# -------------------------------

OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "power": power,
    "root": root,
    "modulus": modulus,
    "int_divide": int_divide,
    "percent": percent,
    "abs_diff": abs_diff,
}


def get_operation(name: str):
    """
    Factory method to return the correct operation function
    based on the provided name.

    Raises:
        OperationError: if the operation name is invalid.
    """
    op = OPERATIONS.get(name)
    if not op:
        raise OperationError(f"Operation '{name}' is not supported.")
    return op
