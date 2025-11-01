import pytest
from app.input_validators import validate_number
from app.exceptions import ValidationError


def test_validate_number_good():
    # Valid numbers should pass
    assert validate_number("5") == 5.0
    assert validate_number("-3.2", max_value=10) == -3.2


def test_validate_number_invalid_string():
    # Non-numeric strings should raise ValidationError
    with pytest.raises(ValidationError):
        validate_number("abc")


def test_validate_number_too_large():
    # Values exceeding max_value should raise ValidationError
    with pytest.raises(ValidationError):
        validate_number("9999", max_value=10)
