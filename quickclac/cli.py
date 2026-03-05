from __future__ import annotations

from quickcalc.calculator import Calculator


def _parse_number(text: str) -> float:
    return float(text.strip())


def run_cli_line(calc: Calculator, line: str) -> str:
    """
    One-line command interface.
    Supported:
      - "<a> + <b>"
      - "<a> - <b>"
      - "<a> * <b>"
      - "<a> / <b>"
      - "C" to clear
    Returns display string.
    """
    line = line.strip()

    if line.upper() == "C":
        calc.clear()
        return "0"

    # very small parser: split by operator
    for op in ["+", "-", "*", "/"]:
        if op in line:
            left, right = line.split(op, 1)
            a = _parse_number(left)
            b = _parse_number(right)

            try:
                if op == "+":
                    result = calc.add(a, b)
                elif op == "-":
                    result = calc.sub(a, b)
                elif op == "*":
                    result = calc.mul(a, b)
                else:
                    result = calc.div(a, b)
            except ZeroDivisionError:
                return "Error: division by zero"

            # Display without trailing .0 when integer
            if result.is_integer():
                return str(int(result))
            return str(result)

    return "Error: invalid input"