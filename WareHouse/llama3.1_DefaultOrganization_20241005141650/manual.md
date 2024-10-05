**Dice Game Manual**

# Introduction
Welcome to the Dice Game! This is a simple text-based command-line application that simulates a dice rolling game using Domain Driven Design (DDD). In this manual, we will guide you through the main functions of the software, how to install environment dependencies, and how to use/play it.

## Main Functions

### 1. Player Creation
To start playing, you need to create a player by providing your name. You can do this by running the command `python main.py` in your terminal. A prompt will appear asking for your name. Enter your name, and it will be validated using the `validate_player_name` function from the `utils` module.

### 2. Dice Rolling
Once you have created a player, you can roll the dice by clicking the "Roll" button on the GUI application. Each die will generate a random number between 1 and 6. The values of all five dice are displayed, and their sum is calculated and printed to the console.

### 3. Score Calculation
The score of each player is incremented by the total value of the rolled dice. You can roll the dice multiple times to increase your score.

## Installing Environment Dependencies

To run the Dice Game, you need to have Python installed on your computer (version 3.8 or higher). Additionally, you need to install the following dependencies:

* `tkinter`: for creating the GUI application
* `unittest`: for unit testing

You can install these dependencies by running the following command in your terminal:
```bash
pip install tkinter unittest
```
or
```bash
conda install tk -c conda-forge
conda install pytest
```

## Using/Playing the Game

To play the Dice Game, follow these steps:

1. Run `python main.py` in your terminal to start the GUI application.
2. Enter your name when prompted to create a player.
3. Click the "Roll" button to roll the dice and display their values.
4. Repeat step 3 multiple times to increase your score.
5. You can quit the game by closing the GUI application.

## Contributing

If you would like to contribute to the development of this game, please feel free to open an issue or submit a pull request on our GitHub repository: [https://github.com/your-username/dice-game](https://github.com/your-username/dice-game).

Happy playing!