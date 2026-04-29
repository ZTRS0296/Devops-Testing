from src.calculator import add, mul, sub


def test_add() -> None:
    assert add(2, 3) == 5


def test_sub() -> None:
    assert sub(10, 4) == 6


def test_mul() -> None:
    assert mul(6, 7) == 42
