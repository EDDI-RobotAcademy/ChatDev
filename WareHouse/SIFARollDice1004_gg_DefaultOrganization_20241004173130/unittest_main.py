import unittest
class TestRollDiceApp(unittest.TestCase):
    def setUp(self):
        self.app = RollDiceApp(None)
    def test_calculate_statistics(self):
        calculator = StatisticsCalculator()
        rolls_list = [Roll(1) for _ in range(5)]
        result = calculator.calculate(rolls_list)
        # Verify that the total is calculated correctly.
        self.assertEqual(result["Total"], sum([roll.value for roll in rolls_list]))
        # Verify that the count is incremented correctly.
        self.assertEqual(result["Count"], len(rolls_list))
if __name__ == '__main__':
    unittest.main()