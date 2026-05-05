# devops-dummy-python

A small Python calculator project used for DevOps and CI/CD practice.

## Features

- Basic operations: `add`, `sub`, `mul`, `div`
- Safe expression evaluator for `+`, `-`, `*`, `/`, and parentheses
- Command-line interface for quick calculations
- Pytest test suite for unit and parser tests

## Project Structure

- `src/calculator.py` - Core calculator logic
- `src/cli.py` - Command-line interface
- `tests/test_calculator.py` - Calculator unit tests
- `tests/test_cli.py` - CLI parser tests

## Prerequisites

- Python 3.10+
- `pip`

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run Tests

```bash
pytest -q
```

## Usage

### 1) Operation mode

```bash
python -m src.cli calc add 2 3
python -m src.cli calc div 10 4
```

### 2) Expression mode

```bash
python -m src.cli expr "(2 + 3) * 4 - 6 / 2"
```

## Notes

- Division by zero raises `ZeroDivisionError`.
- Expression evaluation rejects unsafe syntax (for example function calls).
