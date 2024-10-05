# utils.py
'''
Helper functions for input validation and other tasks.
'''
import re
def validate_player_name(name):
    '''
    Validate the player's name.
    Args:
        name (str): The player's name.
    Returns:
        bool: True if the name is valid, False otherwise.
    '''
    return len(re.match("^[a-zA-Z ]+$", name)) > 0
def is_positive_integer(n):
    '''
    Check if a string represents a positive integer.
    Args:
        n (str): The string to check.
    Returns:
        bool: True if the string represents a positive integer, False otherwise.
    '''
    try:
        int_val = int(n)
        return int_val > 0
    except ValueError:
        return False