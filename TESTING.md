# Testing Strategy (Quick-Calc)

## What was tested
- Core calculation logic (addition, subtraction, multiplication, division).
- Edge cases such as division by zero, negative numbers, decimals, and large values.
- Integration between the input layer (CLI parsing) and the calculator logic:
  - a full user-like calculation flow
  - clear (C) behavior after a computation
  - graceful division by zero message in CLI

## What was not tested (and why)
- A graphical user interface (GUI): the assignment focuses on code quality and testing, not UI complexity.
- Performance and load testing: Quick-Calc is a small application with trivial computation cost.
- Security testing: there is no network access, user accounts, or sensitive data.

## Relation to Lecture 3 Concepts

### Testing Pyramid
Most tests are unit tests (fast, isolated, many). Only a small number are integration tests (slower, cover multiple components). This matches the testing pyramid idea: a broad base of unit tests and fewer higher-level tests.

### Black-box vs White-box Testing
- Unit tests are closer to white-box testing: they directly call methods like `add()` or `div()` and verify expected outputs and exceptions.
- Integration tests are closer to black-box testing: they treat the CLI function like an input/output interface and verify the displayed result without focusing on internal state.

### Functional vs Non-Functional Testing
- Functional testing: verifying correct results for each operation and correct behavior for clear and division by zero.
- Non-functional testing intentionally not covered: performance, scalability, and security are not relevant for a small offline calculator.

### Regression Testing
This test suite can be run after any future change (e.g., refactoring the parser or adding new operations). If a change breaks an existing behavior (like division by zero handling), tests will fail and immediately reveal the regression.

## Test Results Summary

| Test name                                   | Type        | Status |
|--------------------------------------------|-------------|--------|
| test_addition                               | Unit        | Pass   |
| test_subtraction                            | Unit        | Pass   |
| test_multiplication                         | Unit        | Pass   |
| test_division                               | Unit        | Pass   |
| test_division_by_zero_raises                | Unit        | Pass   |
| test_negative_numbers                       | Unit        | Pass   |
| test_decimal_numbers                        | Unit        | Pass   |
| test_very_large_numbers                     | Unit        | Pass   |
| test_clear_resets_to_zero                   | Unit        | Pass   |
| test_full_user_interaction_addition         | Integration | Pass   |
| test_clear_after_calculation_resets_display | Integration | Pass   |
| test_division_by_zero_is_graceful_in_cli    | Integration | Pass   |