"""Small demo module for Redmineflux DevOps integration."""

from __future__ import annotations

import ast
from typing import Union

Number = Union[int, float]


class UnsafeExpressionError(ValueError):
    """Raised when an expression includes unsupported syntax."""


def add(a: Number, b: Number) -> Number:
    return a + b


def sub(a: Number, b: Number) -> Number:
    return a - b


def mul(a: Number, b: Number) -> Number:
    return a * b


def div(a: Number, b: Number) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def evaluate_expression(expression: str) -> Number:
    """Evaluate a safe arithmetic expression using +, -, *, / and parentheses."""
    tree = ast.parse(expression, mode="eval")
    return _eval_node(tree.body)


def _eval_node(node: ast.AST) -> Number:
    if isinstance(node, ast.BinOp) and isinstance(
        node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)
    ):
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if right == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return left / right

    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = _eval_node(node.operand)
        return value if isinstance(node.op, ast.UAdd) else -value

    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    raise UnsafeExpressionError(
        "Only numbers and +, -, *, /, parentheses are allowed"
    )
