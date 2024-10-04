# score_manager.py
'''
Class to manage the total score.
'''
class ScoreManager:
    def __init__(self):
        self.total_score = 0
    def update_score(self, new_score):
        # Update total score with new score
        self.total_score += new_score
    def get_total_score(self):
        return self.total_score