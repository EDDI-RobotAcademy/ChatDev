# LANGUAGE: Python
'''
DOCSTRING: Implementation of the Dice class with improved ID generation and face value regeneration.
'''
import uuid
import random
class id_generator:
    """
    A utility class to generate unique IDs for each instance of the Dice class.
    """
    def __init__(self):
        pass
    def generate_id(self):
        return str(uuid.uuid4())
class Dice:
    def __init__(self, id_generator=id_generator()):
        self.id = id_generator.generate_id()  # Generate a new ID upon creation
        self.face_value = random.randint(1, 6)  # Regenerate face value
    def roll(self):
        """
        Returns the current face value of the Dice after regenerating a new one.
        """
        self.face_value = random.randint(1, 6)  # Regenerate face value upon each roll
        return self.face_value
if __name__ == "__main__":
    die = Dice()
    print("Dice rolled once:", die.roll())
    for _ in range(5):  # Roll the dice five more times
        print("\nNext roll:", die.roll())