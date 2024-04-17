import pytest
from fuel import convert, gauge


def test_convert_valid_input():
    assert convert("3/4") == 75


def test_convert_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")


def test_convert_invalid_input_format():
    with pytest.raises(ValueError):
        convert("3")


def test_convert_invalid_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("5/3")


def test_gauge_below_1():
    assert gauge(0) == "E"


def test_gauge_above_99():
    assert gauge(100) == "F"


def test_gauge_between_1_and_99():
    assert gauge(50) == "50%"
