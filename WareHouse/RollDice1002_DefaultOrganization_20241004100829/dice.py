# dice.py
'''A Dice object has two faces (e.g., 1 and 6) and can have a value between 1 and 6.'''
class Dice:
    def __init__(self):
        self.faces = ["one", "two", "three", "four", "five", "six"]
        self.value = 0
    def roll(self):
        # Generate a random face
        face_index = random.randint(0, len(self.faces) - 1)
        self.value = face_index + 1
        return self.value