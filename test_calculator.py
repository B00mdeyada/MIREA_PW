import unittest
import math

from calculator import add, subtract, multiply, divide, power, sqrt, factorial


class TestCalculatorFunctions(unittest.TestCase):

    # Тестирование add
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -5), -10)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1.5, 2.5), 4.0)
        self.assertEqual(add(0, 5), 5)  # Проверка с нулём
        self.assertEqual(add(1000000, 1000000), 2000000)  # Большие числа

    # Тестирование subtract
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-3, -5), 2)
        self.assertEqual(subtract(10, -10), 20)  # Тест с отрицательным числом
        self.assertEqual(subtract(1000000, 1), 999999)  # Большие числа

    # Тестирование multiply
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 3), 0)
        self.assertEqual(multiply(-2, -2), 4)
        self.assertEqual(multiply(1.5, 2), 3.0)
        self.assertEqual(multiply(1000, 1000), 1000000)
        self.assertEqual(multiply(0, 0), 0)  # Тест с двумя нулями

    # Тестирование divide
    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(3, 1), 3)
        self.assertEqual(divide(-6, -3), 2)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(0, 1), 0)  # Деление на 1
        self.assertEqual(divide(1000000, 2), 500000)  # Большие числа
        with self.assertRaises(ValueError):
            divide(1, 0)  # Деление на 0

    # Тестирование power
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(3, -2), 1/9)
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(2, 0.5), math.sqrt(2))
        self.assertEqual(power(1000, 3), 1000000000)  # Большое число
        self.assertEqual(power(0, 0), 1)  # Особый случай: 0 в степени 0

    # Тестирование sqrt
    def test_sqrt(self):
        self.assertEqual(sqrt(4), 2)
        self.assertEqual(sqrt(9), 3)
        self.assertEqual(sqrt(0), 0)  # Квадратный корень из нуля
        self.assertEqual(sqrt(16), 4)
        self.assertEqual(sqrt(2), math.sqrt(2))  # Тест с нецелым числом
        with self.assertRaises(ValueError):
            sqrt(-4)  # Невозможный корень из отрицательного числа

    # Тестирование factorial
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(10), 3628800)  # Большое число
        with self.assertRaises(ValueError):
            factorial(-1)  # Невозможный факториал отрицательного числа

if __name__ == "__main__":
    unittest.main()
