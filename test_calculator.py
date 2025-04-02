import unittest
from unittest.mock import patch
from calculator import calculator, add, subtract, multiply, divide, power, sqrt, factorial

class TestCalculatorFunctionality(unittest.TestCase):
    # Тестирование калькулятора через mock для ввода и вывода

    @patch('builtins.input', side_effect=['1', '2', '3'])  # Симуляция ввода для операций
    @patch('builtins.print')  # Мокаем print
    def test_calculator_addition(self, mock_print, mock_input):
        # Тест для сложения
        calculator()
        mock_input.assert_any_call('Enter choice (1/2/3/4/5/6/7): ')
        mock_input.assert_any_call('Enter first number: ')
        mock_input.assert_any_call('Enter second number: ')
        
        # Проверка, что вывод корректен
        mock_print.assert_any_call('Result: 5.0')  # Для 2 + 3 = 5.0
        
    @patch('builtins.input', side_effect=['2', '5', '3'])
    @patch('builtins.print')
    def test_calculator_subtraction(self, mock_print, mock_input):
        # Тест для вычитания
        calculator()
        mock_input.assert_any_call('Enter choice (1/2/3/4/5/6/7): ')
        mock_input.assert_any_call('Enter first number: ')
        mock_input.assert_any_call('Enter second number: ')
        
        # Проверка, что вывод корректен
        mock_print.assert_any_call('Result: 2.0')  # Для 5 - 3 = 2.0

    @patch('builtins.input', side_effect=['3', '3', '2'])
    @patch('builtins.print')
    def test_calculator_multiplication(self, mock_print, mock_input):
        # Тест для умножения
        calculator()
        mock_input.assert_any_call('Enter choice (1/2/3/4/5/6/7): ')
        mock_input.assert_any_call('Enter first number: ')
        mock_input.assert_any_call('Enter second number: ')
        
        # Проверка, что вывод корректен
        mock_print.assert_any_call('Result: 6.0')  # Для 3 * 2 = 6.0

    @patch('builtins.input', side_effect=['4', '10', '2'])
    @patch('builtins.print')
    def test_calculator_division(self, mock_print, mock_input):
        # Тест для деления
        calculator()
        mock_input.assert_any_call('Enter choice (1/2/3/4/5/6/7): ')
        mock_input.assert_any_call('Enter first number: ')
        mock_input.assert_any_call('Enter second number: ')
        
        # Проверка, что вывод корректен
        mock_print.assert_any_call('Result: 5.0')  # Для 10 / 2 = 5.0

    @patch('builtins.input', side_effect=['5', '2', '3'])
    @patch('builtins.print')
    def test_calculator_power(self, mock_print, mock_input):
        # Тест для степени
        calculator()
        mock_input.assert_any_call('Enter choice (1/2/3/4/5/6/7): ')
        mock_input.assert_any_call('Enter first number: ')
        mock_input.assert_any_call('Enter second number: ')
        
        # Проверка, что вывод корректен
        mock_print.assert_any_call('Result: 8.0')  # Для 2 ** 3 = 8.0

    @patch('builtins.input', side_effect=['6', '4'])
    @patch('builtins.print')
    def test_calculator_sqrt(self, mock_print, mock_input):
        # Тест для квадратного корня
        calculator()
        mock_input.assert_any_call('Enter choice (1/2/3/4/5/6/7): ')
        mock_input.assert_any_call('Enter a number: ')
        
        # Проверка, что вывод корректен
        mock_print.assert_any_call('Result: 2.0')  # Квадратный корень из 4

    @patch('builtins.input', side_effect=['7', '5'])
    @patch('builtins.print')
    def test_calculator_factorial(self, mock_print, mock_input):
        # Тест для факториала
        calculator()
        mock_input.assert_any_call('Enter choice (1/2/3/4/5/6/7): ')
        mock_input.assert_any_call('Enter an integer: ')
        
        # Проверка, что вывод корректен
        mock_print.assert_any_call('Result: 120')  # Факториал от 5

    @patch('builtins.input', side_effect=['8'])
    @patch('builtins.print')
    def test_calculator_invalid_choice(self, mock_print, mock_input):
        # Тест для некорректного выбора
        calculator()
        mock_input.assert_any_call('Enter choice (1/2/3/4/5/6/7): ')
        mock_print.assert_any_call("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    unittest.main()
