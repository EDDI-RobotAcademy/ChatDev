# calculation.py
'''
Contains functions for performing mathematical calculations.
Ensures robust handling of division by zero and invalid inputs.
'''
import numexpr as ne  # Fixed import statement
def add(num1, num2):
    """
    Adds two numbers together.
    Args:
        num1 (int or float): The first number to add.
        num2 (int or float): The second number to add.
    Returns:
        int or float: The sum of the two numbers.
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Error: Invalid input")
    return num1 + num2
def subtract(num1, num2):
    """
    Subtracts one number from another.
    Args:
        num1 (int or float): The first number to subtract from.
        num2 (int or float): The second number to subtract.
    Returns:
        int or float: The difference between the two numbers.
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Error: Invalid input")
    return num1 - num2
def multiply(num1, num2):
    """
    Multiplies two numbers together.
    Args:
        num1 (int or float): The first number to multiply.
        num2 (int or float): The second number to multiply.
    Returns:
        int or float: The product of the two numbers.
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Error: Invalid input")
    return num1 * num2
def divide(num1, num2):
    """
    Divides one number by another.
    Args:
        num1 (int or float): The dividend.
        num2 (int or float): The divisor.
    Returns:
        int or float: The quotient of the division.
    Raises:
        ValueError: If the divisor is zero.
    """
    if num2 == 0:
        raise ValueError("Error: Division by zero! Please ensure you're not trying to divide by zero.")
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Error: Invalid input")
    return num1 / num2