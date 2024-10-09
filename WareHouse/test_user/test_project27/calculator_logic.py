# python
'''
Calculator Logic Class
This class handles arithmetic calculations based on user input.
'''
class CalculatorLogic:
    def calculate(self, num1: float, operator: str, num2: float) -> float:
        try:
            num1 = float(num1)
            num2 = float(num2)
            if operator == '+':
                return num1 + num2
            elif operator == '-':
                return num1 - num2
            elif operator == '*':
                return num1 * num2
            elif operator == '/':
                if num2 != 0:
                    return num1 / num2
                else:
                    raise ZeroDivisionError("Cannot divide by zero")
        except ValueError as e:
            raise ValueError("Invalid input values. Please enter numeric values.")