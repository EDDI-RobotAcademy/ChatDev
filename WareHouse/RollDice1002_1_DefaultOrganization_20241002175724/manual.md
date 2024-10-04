# LangChain: A User Manual

Welcome to LangChain, a library for building applications with Large Language Models (LLMs) through composability. This manual will guide you through the installation process, introduce the main functions of the software, and provide examples on how to use it.

## Installing Environment Dependencies

To install LangChain, you'll need to have Python 3.8 or higher installed on your machine. You can do this by running the following command in your terminal:

```bash
pip install langchain
```

or

```bash
conda install langchain -c conda-forge
```

## Main Functions of LangChain

LangChain provides a range of functions for building applications with LLMs, including:

*   **Roller:** A class that manages multiple dice rolls. It allows you to roll dice and reset their values.
*   **Dice:** A class that simulates the roll of a standard six-sided die.

## Example Usage

### Roller Class

The Roller class is used to manage multiple dice rolls. Here's an example of how to use it:

```python
from langchain.roller import Roller

def main():
    # Create a new instance of the Roller class
    roller = Roller()

    # Roll all specified dice and return their results
    results = roller.roll()
    print(results)

if __name__ == "__main__":
    main()
```

This code will roll all dice in the `roller` object and print out their results.

### Dice Class

The Dice class simulates the roll of a standard six-sided die. Here's an example of how to use it:

```python
from langchain.dice import Dice

def main():
    # Create a new instance of the Dice class
    die = Dice()

    # Roll this die and get its result
    result = die.roll()
    print(result)

if __name__ == "__main__":
    main()
```

This code will roll the `die` object and print out the result.

## Resetting Rolled Values

To reset the rolled values for each die, you can call the `reset()` method on the `roller` object:

```python
from langchain.roller import Roller

def main():
    # Create a new instance of the Roller class
    roller = Roller()

    # Roll all specified dice and return their results
    results = roller.roll()
    print(results)

    # Reset the rolled values for each die
    roller.reset()

if __name__ == "__main__":
    main()
```

This code will roll all dice in the `roller` object, reset their rolled values, and then re-roll them.