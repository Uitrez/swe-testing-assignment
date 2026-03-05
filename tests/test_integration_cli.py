from quickcalc.calculator import Calculator
from quickcalc.cli import run_cli_line


def test_full_user_interaction_addition():
    calc = Calculator()
    # Simulate: enter "5", press "+", enter "3", "="
    # In our CLI format it's: "5 + 3"
    output = run_cli_line(calc, "5 + 3")
    assert output == "8"


def test_clear_after_calculation_resets_display():
    calc = Calculator()
    assert run_cli_line(calc, "9 * 2") == "18"
    assert run_cli_line(calc, "C") == "0"


def test_division_by_zero_is_graceful_in_cli():
    calc = Calculator()
    assert run_cli_line(calc, "5 / 0") == "Error: division by zero"