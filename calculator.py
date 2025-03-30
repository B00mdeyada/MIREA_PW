import math

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: Division by zero"
def power(a, b): return a ** b
def sqrt(a): return math.sqrt(a) if a >= 0 else "Error: Negative sqrt"
def factorial(a): return math.factorial(a) if a >= 0 else "Error: Negative factorial"

OPERATIONS = {
    "1": ("Add", add),
    "2": ("Subtract", subtract),
    "3": ("Multiply", multiply),
    "4": ("Divide", divide),
    "5": ("Power", power),
    "6": ("Square Root", lambda x: sqrt(x)),
    "7": ("Factorial", lambda x: factorial(int(x)))
}

def calculator():
    print("Advanced Calculator")
    for key, (name, _) in OPERATIONS.items():
        print(f"{key}. {name}")

    choice = input("Enter choice: ")
    operation = OPERATIONS.get(choice)

    if not operation:
        print("Invalid input")
        return

    func = operation[1]
    try:
        if choice in {"6", "7"}:
            num = float(input("Enter a number: "))
            print(f"Result: {func(num)}")
        else:
            num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
            print(f"Result: {func(num1, num2)}")
    except ValueError:
        print("Error: Invalid input")

if __name__ == "__main__":
    calculator()
