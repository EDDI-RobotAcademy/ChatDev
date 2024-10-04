# Importing necessary libraries
class RollResult:
    def __init__(self):
        """
        Initializes the RollResult object with an empty list to store roll results.
        Attributes:
            results (list): The list of roll results.
        """
        self.results = []
    def add_result(self, result):
        """
        Adds a new result to the list of roll results.
        Args:
            result (int): The new result to be added.
        """
        self.results.append(result)
    def get_results(self):
        """
        Returns the list of roll results as a comma-separated string.
        Returns:
            str: The list of roll results as a comma-separated string.
        """
        return ", ".join(map(str, self.results))