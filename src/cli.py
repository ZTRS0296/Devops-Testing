"""Command-line interface for the demo calculator."""

from __future__ import annotations

import argparse

from src.calculator import add, div, evaluate_expression, mul, sub


OPERATIONS = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Demo calculator CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    binary_parser = subparsers.add_parser("calc", help="Run binary operation")
    binary_parser.add_argument("operation", choices=OPERATIONS.keys())
    binary_parser.add_argument("a", type=float)
    binary_parser.add_argument("b", type=float)

    expr_parser = subparsers.add_parser("expr", help="Evaluate expression")
    expr_parser.add_argument("expression", type=str)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "calc":
        result = OPERATIONS[args.operation](args.a, args.b)
    else:
        result = evaluate_expression(args.expression)

    print(result)


if __name__ == "__main__":
    main()
