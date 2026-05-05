from src.cli import build_parser


def test_parser_calc_mode() -> None:
    args = build_parser().parse_args(["calc", "add", "2", "3"])
    assert args.command == "calc"
    assert args.operation == "add"
    assert args.a == 2.0
    assert args.b == 3.0


def test_parser_expr_mode() -> None:
    args = build_parser().parse_args(["expr", "2+3*4"])
    assert args.command == "expr"
    assert args.expression == "2+3*4"
