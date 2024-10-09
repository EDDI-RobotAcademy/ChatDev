# LANGUAGE: Python
class MathUtils:
    def arithmetic_operation(self, operation_type, num1, num2):
        if operation_type == "add":
            return num1 + num2
        elif operation_type == "subtract":
            return num1 - num2
        elif operation_type == "multiply":
            return num1 * num2
        elif operation_type == "divide":
            try:
                return num1 / num2
            except ZeroDivisionError as zde:
                raise zde