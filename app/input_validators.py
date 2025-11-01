from .exceptions import ValidationError

def validate_number(value, max_value=None):
    try:
        num = float(value)
    except ValueError as exc:
        raise ValidationError(f"Invalid number: {value}") from exc

    if max_value is not None and abs(num) > max_value:
        raise ValidationError(f"Value {num} exceeds max allowed {max_value}")
    return num
