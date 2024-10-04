# python
'''
Repository for storing and retrieving roll dice data.
'''
import sqlite3
class RollDiceRepository:
    def __init__(self):
        self.conn = sqlite3.connect('roll_dice.db')
        self.cursor = self.conn.cursor()
    def save_roll(self, roll):
        '''
        Save a single roll to the database.
        Args:
            roll (int): The roll value to be saved.
        Returns:
            None
        '''
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS rolls (
                    id INTEGER PRIMARY KEY,
                    roll INTEGER
                )
            ''')
            self.cursor.execute("INSERT INTO rolls VALUES (NULL, ?)", (roll,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error saving roll to database: {e}")
            return False
    def get_rolls(self):
        '''
        Retrieve all the saved rolls from the database.
        Returns:
            list: A list of saved roll values.
        '''
        try:
            self.cursor.execute("SELECT * FROM rolls")
            rows = self.cursor.fetchall()
            rolls = [row[1] for row in rows]
            return rolls
        except sqlite3.Error as e:
            print(f"Error retrieving rolls from database: {e}")
            return []