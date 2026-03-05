from __future__ import annotations


class Calculator:
    """
    Simple stateful calculator:
    - stores current display value
    - supports add/sub/mul/div on two numbers
    - supports clear (C)
    """

    def __init__(self) -> None:
        self.clear()

    def clear(self) -> None:
        self.current = 0.0

    def add(self, a: float, b: float) -> float:
        self.current = a + b
        return self.current

    def sub(self, a: float, b: float) -> float:
        self.current = a - b
        return self.current

    def mul(self, a: float, b: float) -> float:
        self.current = a * b
        return self.current

    def div(self, a: float, b: float) -> float:
        if b == 0:
            # "handles division by zero gracefully"
            raise ZeroDivisionError("Cannot divide by zero")
        self.current = a / b
        return self.current