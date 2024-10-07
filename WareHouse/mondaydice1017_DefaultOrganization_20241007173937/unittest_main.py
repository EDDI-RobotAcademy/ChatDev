# LANGUAGE: Python3
"""
DOCSTRING:
Player unit test class to update scores and handle invalid inputs.
"""
import unittest
class Player(unittest.TestCase):
    def setUp(self):
        self.player = Player()
    def test_update_score(self):
        # Arrange: Initialize the player with a valid score value
        score_value = 10
        # Act: Call the update_score method to increment the score
        result = self.player.update_score(score_value)
        # Assert: Verify that scores are incremented correctly
        self.assertEqual(result, score_value + 1)
if __name__ == "__main__":
    unittest.main()