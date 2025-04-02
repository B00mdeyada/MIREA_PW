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


def calculator():
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
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            return

        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            try:
                print(f"Result: {divide(num1, num2)}")
            except ValueError as e:
                print(e)
        elif choice == '5':
            print(f"Result: {power(num1, num2)}")
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
    calculator()
