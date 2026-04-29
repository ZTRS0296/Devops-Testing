from src.calculator import add, sub


def test_add() -> None:
    assert add(2, 3) == 5


def test_sub() -> None:
    assert sub(10, 4) == 6
