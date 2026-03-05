import pytest
from quickcalc.calculator import Calculator


def test_addition():
    c = Calculator()
    assert c.add(5, 3) == 8


def test_subtraction():
    c = Calculator()
    assert c.sub(10, 4) == 6


def test_multiplication():
    c = Calculator()
    assert c.mul(6, 7) == 42


def test_division():
    c = Calculator()
    assert c.div(8, 2) == 4


# Edge cases (at least 2)
def test_division_by_zero_raises():
    c = Calculator()
    with pytest.raises(ZeroDivisionError):
        c.div(5, 0)


def test_negative_numbers():
    c = Calculator()
    assert c.add(-5, -3) == -8


def test_decimal_numbers():
    c = Calculator()
    assert c.mul(2.5, 2) == 5.0


def test_very_large_numbers():
    c = Calculator()
    assert c.add(10**12, 10**12) == 2 * 10**12


def test_clear_resets_to_zero():
    c = Calculator()
    c.add(9, 1)
    c.clear()
    assert c.current == 0.0