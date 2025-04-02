import unittest
import math

# Предполагаем, что код калькулятора импортирован
from calculator import add, subtract, multiply, divide, power, sqrt, factorial


class TestCalculatorFunctions(unittest.TestCase):

    # Тестирование add
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -5), -10)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1.5, 2.5), 4.0)  # Тест с дробными числами

    # Тестирование subtract
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-3, -5), 2)  # Тест с отрицательными числами

    # Тестирование multiply
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 3), 0)
        self.assertEqual(multiply(-2, -2), 4)
        self.assertEqual(multiply(1.5, 2), 3.0)  # Тест с дробными числами
        self.assertEqual(multiply(1000, 1000), 1000000)  # Тест с большими числами

    # Тестирование divide
    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(3, 1), 3)
        self.assertEqual(divide(-6, -3), 2)  # Тест с отрицательными числами
        self.assertEqual(divide(5, 2), 2.5)  # Тест с дробными числами
        with self.assertRaises(ValueError):
            divide(1, 0)  # Тест деления на ноль

    # Тестирование power
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(3, -2), 1/9)
        self.assertEqual(power(0, 5), 0)  # Тест с нулем в основании
        self.assertEqual(power(2, 0.5), math.sqrt(2))  # Тест с дробным показателем степени

    # Тестирование sqrt
    def test_sqrt(self):
        self.assertEqual(sqrt(4), 2)
        self.assertEqual(sqrt(9), 3)
        self.assertEqual(sqrt(0), 0)  # Тест с нулем
        self.assertEqual(sqrt(16), 4)  # Тест с квадратом целого числа
        with self.assertRaises(ValueError):
            sqrt(-4)  # Тест с отрицательным числом

    # Тестирование factorial
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)  # Тест для минимального положительного числа
        self.assertEqual(factorial(3), 6)  # Тест для маленького числа
        with self.assertRaises(ValueError):
            factorial(-1)  # Тест для отрицательного числа

if __name__ == "__main__":
    unittest.main()
