class CalculatorError(Exception):
    """Base class for calculator errors."""


class OperationError(CalculatorError):
    """Raised when an operation fails or is not supported."""


class ValidationError(CalculatorError):
    """Raised when input is invalid."""
