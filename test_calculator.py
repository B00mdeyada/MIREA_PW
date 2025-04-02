import pytest
from unittest.mock import patch
from calculator import add, subtract, multiply, divide, power, sqrt, factorial, calculator


# Тесты для основных операций
def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(0, 0) == 0
    assert add(-2, -3) == -5


def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(-5, 2) == -7
    assert subtract(5, -2) == 7
    assert subtract(0, 0) == 0
    assert subtract(-5, -5) == 0


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 4) == 0
    assert multiply(3, 0) == 0
    assert multiply(-3, 4) == -12
    assert multiply(-3, -4) == 12


def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 5) == 2
    assert divide(0, 5) == 0
    assert divide(-10, 2) == -5
    assert divide(10, -2) == -5
    with pytest.raises(ValueError):
        divide(10, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(2, 0) == 1
    assert power(0, 2) == 0
    assert power(2, -3) == 0.125
    assert power(-2, 2) == 4
    assert power(-2, 3) == -8


def test_sqrt():
    assert sqrt(16) == 4
    assert sqrt(0) == 0
    assert sqrt(1) == 1
    with pytest.raises(ValueError):
        sqrt(-1)


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6
    with pytest.raises(ValueError):
        factorial(-1)


# Тестирование калькулятора с мокированием ввода
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


# Дополнительные тесты
def test_add_large_numbers():
    assert add(10**6, 10**6) == 2 * 10**6


def test_subtract_large_numbers():
    assert subtract(10**6, 10**5) == 900000


def test_multiply_large_numbers():
    assert multiply(10**3, 10**3) == 10**6


def test_divide_large_numbers():
    assert divide(10**6, 10**3) == 1000


def test_power_edge_cases():
    assert power(2, 0) == 1  # любое число в нулевой степени равно 1
    assert power(0, 0) == 1  # 0^0 принято считать равным 1 в математике
    assert power(2, -3) == 1/8  # 2^(-3) = 1/8
