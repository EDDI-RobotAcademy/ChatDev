"""
Utility functions for the calculator application.
"""
def add(x, y):
    """Return the sum of two numbers."""
    return x + y
def subtract(x, y):
    """Return the difference of two numbers."""
    return x - y
def multiply(x, y):
    """Return the product of two numbers."""
    return x * y
def divide(x, y):
    """
    Return the quotient of two numbers. Raise ZeroDivisionError if the divisor is zero.
    Adds input validation to ensure both x and y are numeric.
    If either x or y is not numeric, returns an error message.
    """
    # Add input validation to ensure both x and y are numeric
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        return "Error: Both inputs must be numbers"
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y