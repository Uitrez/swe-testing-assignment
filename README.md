# Quick-Calc (swe-testing-assignment)

Quick-Calc is a minimal calculator application that supports addition, subtraction, multiplication, division (with graceful handling of division by zero), and a clear (C) operation. The focus of this project is not the UI, but clean logic, a solid testing strategy (unit + integration), and a professional Git/GitHub workflow.

## Setup

### Requirements
- Python 3.10+

### Install dependencies
```bash
python -m pip install pytest

Run the application (example usage)

This project exposes a small command-style interface through run_cli_line() in quickcalc/cli.py.

Example (in Python):

from quickcalc.calculator import Calculator
from quickcalc.cli import run_cli_line

calc = Calculator()
print(run_cli_line(calc, "5 + 3"))  # 8
print(run_cli_line(calc, "C"))      # 0

## How to run tests

Run all tests with:

pytest

"Testing framework research (Pytest vs Unittest)

Python provides unittest in the standard library. It is stable, widely used, and does not require external installation. It encourages an object-oriented style (TestCase classes) and provides many built-in assertions. However, test code can become verbose, and writing concise parameterized tests usually requires extra work or patterns.

pytest is a popular third-party testing framework known for its simple syntax, powerful fixtures, and excellent reporting. Tests can be written as plain functions with standard assert, which is beginner-friendly. It also supports parameterization and fixtures in a very clean way, which helps scale the test suite without repeating code.

For this project, pytest was chosen because it reduces boilerplate, keeps tests readable, and makes it easy to separate unit tests (core logic) from integration tests (CLI + logic working together)."