# error_handling_example.py
'''
This module contains an example of how to add error handling for empty strings.
'''
from calculator import calculate_result
def calculate_and_display(expression):
    try:
        result = calculate_result(expression)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
calculate_and_display("")