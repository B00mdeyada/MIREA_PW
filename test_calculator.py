import pytest
from unittest.mock import patch
import io
import sys
from your_script import (add, subtract, multiply, divide, power, sqrt, 
                        factorial, calculator)  # Замените 'your_script' на имя вашего файла

# Тесты для базовых математических функций
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, -1) == 0
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(6, 2) == 3.0
    assert divide(-6, 2) == -3.0
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        divide(5, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(2, 0) == 1
    assert power(0, 5) == 0

def test_sqrt():
    assert sqrt(4) == 2.0
    assert sqrt(0) == 0.0
    with pytest.raises(ValueError, match="Cannot calculate the square root of a negative number"):
        sqrt(-1)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError, match="Factorial of a negative number is not defined"):
        factorial(-1)

# Тесты для функции calculator с использованием mock ввода-вывода
def test_calculator_add():
    with patch('builtins.input', side_effect=['1', '2', '3']):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculator()
            assert "Result: 5" in fake_out.getvalue()

def test_calculator_subtract():
    with patch('builtins.input', side_effect=['2', '5', '3']):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculator()
            assert "Result: 2" in fake_out.getvalue()

def test_calculator_multiply():
    with patch('builtins.input', side_effect=['3', '2', '3']):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculator()
            assert "Result: 6" in fake_out.getvalue()

def test_calculator_divide():
    with patch('builtins.input', side_effect=['4', '6', '2']):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculator()
            assert "Result: 3.0" in fake_out.getvalue()

def test_calculator_divide_by_zero():
    with patch('builtins.input', side_effect=['4', '5', '0']):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculator()
            assert "Division by zero is not allowed" in fake_out.getvalue()

def test_calculator_power():
    with patch('builtins.input', side_effect=['5', '2', '3']):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculator()
            assert "Result: 8" in fake_out.getvalue()

def test_calculator_sqrt():
    with patch('builtins.input', side_effect=['6', '4']):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculator()
            assert "Result: 2.0" in fake_out.getvalue()

def test_calculator_sqrt_negative():
    with patch('builtins.input', side_effect=['6', '-1']):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculator()
            assert "Cannot calculate the square root of a negative number" in fake_out.getvalue()

def test_calculator_factorial():
    with patch('builtins.input', side_effect=['7', '5']):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculator()
            assert "Result: 120" in fake_out.getvalue()

def test_calculator_factorial_negative():
    with patch('builtins.input', side_effect=['7', '-1']):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculator()
            assert "Factorial of a negative number is not defined" in fake_out.getvalue()

def test_calculator_invalid_input():
    with patch('builtins.input', side_effect=['8']):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculator()
            assert "Invalid input" in fake_out.getvalue()
