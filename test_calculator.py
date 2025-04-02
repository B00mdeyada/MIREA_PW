import pytest
from unittest.mock import patch
from calculator import add, subtract, multiply, divide, power, sqrt, factorial, calculator


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)


def test_power():
    assert power(2, 3) == 8


def test_sqrt():
    assert sqrt(16) == 4
    with pytest.raises(ValueError):
        sqrt(-1)


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    with pytest.raises(ValueError):
        factorial(-1)


# Тестирование calculator() с мокированным вводом
@pytest.mark.parametrize(
    "inputs, expected_output",
    [
        (["1", "5", "3"], "Result: 8.0"),  # 5 + 3 = 8
        (["2", "10", "7"], "Result: 3.0"),  # 10 - 7 = 3
        (["3", "6", "2"], "Result: 12.0"),  # 6 * 2 = 12
        (["4", "9", "3"], "Result: 3.0"),  # 9 / 3 = 3
        (["5", "2", "4"], "Result: 16.0"),  # 2^4 = 16
        (["6", "25"], "Result: 5.0"),  # sqrt(25) = 5
        (["7", "4"], "Result: 24"),  # 4! = 24
    ],
)
def test_calculator(inputs, expected_output, capsys):
    with patch("builtins.input", side_effect=inputs):
        calculator()  # Запускаем функцию

    captured = capsys.readouterr()  # Читаем, что вывела программа
    assert expected_output in captured.out
