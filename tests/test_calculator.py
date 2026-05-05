import pytest

from src.calculator import UnsafeExpressionError, add, div, evaluate_expression, mul, sub


def test_add() -> None:
    assert add(2, 3) == 5


def test_sub() -> None:
    assert sub(10, 4) == 6


def test_mul() -> None:
    assert mul(6, 7) == 42


def test_div() -> None:
    assert div(10, 4) == 2.5


def test_div_by_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        div(3, 0)


def test_evaluate_expression() -> None:
    assert evaluate_expression("(2 + 3) * 4 - 6 / 2") == 17


def test_evaluate_expression_with_unary_minus() -> None:
    assert evaluate_expression("-5 + 3") == -2


def test_evaluate_expression_rejects_unsafe_syntax() -> None:
    with pytest.raises(UnsafeExpressionError):
        evaluate_expression("__import__('os').system('echo hacked')")
