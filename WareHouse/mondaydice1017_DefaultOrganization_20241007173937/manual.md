manual.md
=====================================

**ChatDev Dice Rolling Game User Manual**
--------------------------------------

Introduction
------------

Welcome to the ChatDev Dice Rolling Game! This manual will guide you through the main features and functionalities of the game.

Main Functions
----------------

The game allows you to simulate a dice rolling experience. The following are the key functions:

*   **Rolling the Dice**: Roll the virtual dice by clicking on the "Reset" button in the GUI.
*   **Updating Scores**: The scores will be updated automatically after each roll.
*   **Resetting Game**: Click on the "Reset" button to restart a new game.

Installation
------------

To run the game, you need to have Python 3 installed on your system. You can install the required dependencies by running:

```
pip install -r requirements.txt
```

Usage
-----

1.  Run the `main.py` script.
2.  A GUI will appear with a "Reset" button and a label displaying current scores.
3.  Click on the "Reset" button to roll the dice.

How it Works
-------------

The game uses a simple design pattern:

*   The `Game` class initializes two players and manages their scores.
*   The `DiceRoller` class simulates rolling a virtual dice, returning a random number between 1 and 6.
*   The `SuggestedImprovements` class updates the player scores after each roll.

Troubleshooting
--------------

If you encounter any issues while running the game, please refer to the following troubleshooting guide:

*   **Error: unable to import tkinter**:
    *   Make sure that Python 3 is installed on your system.
    *   Try reinstalling the `tkinter` package using pip.

Conclusion
----------

The ChatDev Dice Rolling Game is a simple yet engaging application that demonstrates the use of Domain-Driven Design principles in game development. With this manual, you should be able to easily install and play the game.

**Note:** This manual assumes basic knowledge of Python programming concepts. If you're new to Python, we recommend exploring online resources or tutorials before diving into the code.

**Happy Rolling!**