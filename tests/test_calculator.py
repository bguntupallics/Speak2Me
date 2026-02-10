import pytest

from app.services.calculator_service import calculate, parse


class TestParse:
    def test_simple_addition(self):
        assert parse("5 add 3") == [5.0, "+", 3.0]

    def test_simple_subtraction(self):
        assert parse("10 minus 4") == [10.0, "-", 4.0]

    def test_multiplication(self):
        assert parse("6 times 7") == [6.0, "*", 7.0]

    def test_division(self):
        assert parse("20 divide 5") == [20.0, "/", 5.0]

    def test_squared(self):
        assert parse("10 squared") == [10.0, "**", 2.0]

    def test_cubed(self):
        assert parse("3 cubed") == [3.0, "**", 3.0]

    def test_square_root(self):
        assert parse("square root 16") == [0.5, "root", 16.0]

    def test_cube_root(self):
        tokens = parse("cube root 27")
        assert len(tokens) == 3
        assert abs(tokens[0] - 1 / 3) < 0.001
        assert tokens[1] == "root"
        assert tokens[2] == 27.0

    def test_symbol_operators(self):
        assert parse("5 + 3") == [5.0, "+", 3.0]
        assert parse("5 * 3") == [5.0, "*", 3.0]

    def test_word_numbers(self):
        assert parse("five add three") == [5.0, "+", 3.0]

    def test_skips_filler_words(self):
        assert parse("5 divided by 3") == [5.0, "/", 3.0]

    def test_decimal_numbers(self):
        assert parse("3.14 add 2.86") == [3.14, "+", 2.86]


class TestCalculate:
    def test_addition(self):
        assert calculate([5.0, "+", 3.0]) == 8.0

    def test_subtraction(self):
        assert calculate([10.0, "-", 4.0]) == 6.0

    def test_multiplication(self):
        assert calculate([6.0, "*", 7.0]) == 42.0

    def test_division(self):
        assert calculate([20.0, "/", 5.0]) == 4.0

    def test_power(self):
        assert calculate([10.0, "**", 2.0]) == 100.0

    def test_root(self):
        assert calculate([0.5, "root", 16.0]) == 4.0

    def test_division_by_zero(self):
        with pytest.raises(ValueError, match="Division by zero"):
            calculate([5.0, "/", 0.0])

    def test_empty_expression(self):
        with pytest.raises(ValueError, match="Empty expression"):
            calculate([])

    def test_single_number(self):
        assert calculate([42.0]) == 42.0

    def test_incomplete_expression(self):
        with pytest.raises(ValueError, match="Incomplete expression"):
            calculate([5.0, "+"])
