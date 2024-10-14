"""
Simple Calculator App
======================
A basic calculator application that allows users to perform arithmetic operations.
"""
import math
def add(num1: float, num2: float) -> float:
    """
    Adds two numbers.
    Args:
        num1 (float): The first number.
        num2 (float): The second number.
    Returns:
        float: The sum of the two numbers.
    """
    return num1 + num2
def subtract(num1: float, num2: float) -> float:
    """
    Subtracts one number from another.
    Args:
        num1 (float): The first number.
        num2 (float): The second number.
    Returns:
        float: The difference between the two numbers.
    """
    return num1 - num2
def multiply(num1: float, num2: float) -> float:
    """
    Multiplies two numbers.
    Args:
        num1 (float): The first number.
        num2 (float): The second number.
    Returns:
        float: The product of the two numbers.
    """
    return num1 * num2
def divide(num1: float, num2: float) -> float:
    """
    Divides one number by another.
    Args:
        num1 (float): The dividend.
        num2 (float): The divisor.
    Returns:
        float: The quotient of the two numbers. Raises ZeroDivisionError if the divisor is zero.
    """
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return num1 / num2
def calculator() -> None:
    """
    A simple calculator class that allows users to perform basic arithmetic operations.
    Methods:
        add: Adds two numbers.
        subtract: Subtracts one number from another.
        multiply: Multiplies two numbers.
        divide: Divides one number by another.
    """
    while True:
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")
        choice = input("Enter your choice (1-5): ")
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            else:
                try:
                    result = divide(num1, num2)
                except ZeroDivisionError as e:
                    print(e)
                    continue
            print(f"Result: {result}")
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")
if __name__ == "__main__":
    # Call the calculator function directly without trying to call main()
    calculator()