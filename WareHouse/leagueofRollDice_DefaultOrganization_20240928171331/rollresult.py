class RollResult:
    """
    Stores the results of rolling multiple dice.
    Attributes:
        results (list): A list to store the roll results for each die.
    """
    def __init__(self):
        """
        Initializes the RollResult object with an empty list to store roll results.
        """
        self.results = []