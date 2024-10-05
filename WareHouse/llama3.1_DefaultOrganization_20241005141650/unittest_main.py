import unittest
class TestUtils(unittest.TestCase):
    def test_is_positive_integer(self):
        # Arrange
        valid_str = "10"
        invalid_str = "-5"
        # Act
        is_valid = is_positive_integer(valid_str)
        is_invalid = is_positive_integer(invalid_str)
        # Assert
        assert is_valid == True
        assert is_invalid == False
# unittest
if __name__ == '__main__':
    unittest.main()