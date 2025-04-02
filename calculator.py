import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number")
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        raise ValueError("Factorial of a negative number is not defined")
    return math.factorial(a)

def get_numbers_for_basic_operations():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return None, None

def perform_basic_operation(choice, num1, num2):
    if choice == '1':
        return add(num1, num2)
    elif choice == '2':
        return subtract(num1, num2)
    elif choice == '3':
        return multiply(num1, num2)
    elif choice == '4':
        return divide(num1, num2)
    elif choice == '5':
        return power(num1, num2)
    return None

def handle_calculator_input():
    print("Advanced Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    
    choice = input("Enter choice (1/2/3/4/5/6/7): ")
    
    if choice in ('1', '2', '3', '4', '5'):
        num1, num2 = get_numbers_for_basic_operations()
        if num1 is None or num2 is None:
            return
        result = perform_basic_operation(choice, num1, num2)
        print(f"Result: {result}")
    elif choice == '6':
        try:
            num = float(input("Enter a number: "))
            print(f"Result: {sqrt(num)}")
        except ValueError as e:
            print(e)
    elif choice == '7':
        try:
            num = int(input("Enter an integer: "))
            print(f"Result: {factorial(num)}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    handle_calculator_input()
