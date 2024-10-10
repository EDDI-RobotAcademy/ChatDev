"""
This module contains unit tests for the CalculatorModel class.
"""
import unittest
from calculator_model import CalculatorModel
class TestCalculatorModel(unittest.TestCase):
    def test_init(self):
        # Test default values of num1, num2, and operator
        model = CalculatorModel()
        self.assertEqual(model.num1, 0)
        self.assertEqual(model.num2, 0)
        self.assertEqual(model.operator, '')
    def test_set_num1(self):
        # Test setting valid numbers for num1
        model = CalculatorModel()
        model.set_num1(5)
        self.assertEqual(model.num1, 5)
        # Test setting invalid numbers for num1 (integers instead of floats)
        with self.assertRaises(ValueError):
            model.set_num1(3.14)
    def test_set_num2(self):
        # Test setting valid numbers for num2
        model = CalculatorModel()
        model.set_num2(10)
        self.assertEqual(model.num2, 10)
        # Test setting invalid numbers for num2 (integers instead of floats)
        with self.assertRaises(ValueError):
            model.set_num2(3.14)
    def test_set_operator(self):
        # Test setting valid operator
        model = CalculatorModel()
        model.set_operator("+")
        self.assertEqual(model.operator, "+")
        # Test setting invalid operator (character instead of string)
        with self.assertRaises(TypeError):
            model.set_operator(42)
    def test_clear(self):
        # Test clearing the calculator model
        model = CalculatorModel()
        model.set_num1(5)
        model.set_num2(10)
        model.set_operator("+")
        model.clear()
        self.assertEqual(model.num1, 0)
        self.assertEqual(model.num2, 0)
        self.assertEqual(model.operator, "")
    def test_calculate(self):
        # Test calculating with valid inputs
        model = CalculatorModel()
        model.set_num1(5)
        model.set_num2(10)
        model.set_operator("+")
        result = model.calculate()
        self.assertAlmostEqual(result, 15.0)
        # Test calculating with invalid inputs (operator not defined)
        model = CalculatorModel()
        model.set_num1(5)
        model.set_num2(10)
        model.set_operator("^")
        with self.assertRaises(ValueError):
            model.calculate()
class TestCalculatorModelErrors(unittest.TestCase):
    def test_set_num1_error(self):
        # Test setting invalid type for num1
        model = CalculatorModel()
        with self.assertRaises(TypeError):
            model.set_num1("hello")
    def test_set_num2_error(self):
        # Test setting invalid type for num2
        model = CalculatorModel()
        with self.assertRaises(TypeError):
            model.set_num2(42.0)
    def test_set_operator_error(self):
        # Test setting invalid type for operator
        model = CalculatorModel()
        with self.assertRaises(TypeError):
            model.set_operator(3.14)