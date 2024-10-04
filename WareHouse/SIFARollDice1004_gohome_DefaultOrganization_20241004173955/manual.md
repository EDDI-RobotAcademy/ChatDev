**Roll Dice App User Manual**

**Introduction**
===============

Welcome to the Roll Dice App! This user manual will guide you through the main features and functionality of the app.

**Main Functions**
================

1. **Rolling a Dice**: Enter the number of sides on the dice, click the "Roll Dice" button, and see the result in real-time.
2. **Customizable Input**: Adjust the number of sides to roll the dice with.
3. **Interactive Graph**: Visualize each new roll with an updated graph.

**Installing Environment Dependencies**
=====================================

To run the Roll Dice App, you'll need to install the required libraries. Follow these steps:

1. **Python Installation**: Ensure Python 3.x is installed on your system.
2. **Package Manager**: Install pip (the Python package manager) if it's not already available.
3. **Required Libraries**:
	* `dash==2.6.0`: A web framework for building reactive, real-time data visualization apps.
	* `plotly>=5.4.0`: A high-level, declarative graphing library that supports interactive features.
	* `pandas>=1.1.4`: A powerful data analysis and manipulation library.
	* `random==0.8.3`: A library for generating random numbers.
	* `numpy==1.19.2`: A library for efficient numerical computation.
	* `unittest==3.9.0`: A unit testing framework for Python.

**Installation Steps**

You can install the required libraries using pip:
```bash
pip install dash plotly pandas random numpy unittest
```
Alternatively, you can use conda (for Anaconda users):
```bash
conda install -c conda-forge dash plotly pandas random numpy unittest
```
**Using the Roll Dice App**
==========================

1. **Launch the App**: Run `python main.py` in your terminal or command prompt.
2. **Interact with the App**: Enter a number of sides, click the "Roll Dice" button, and explore the interactive graph.

**Troubleshooting**
------------------

If you encounter any issues while running the app, please consult the [FAQ section](#faq) below.

**FAQ**
=====

Q: What libraries are required to run the Roll Dice App?
A: The app requires `dash`, `plotly`, `pandas`, `random`, `numpy`, and `unittest` libraries.

Q: How do I install the required libraries?
A: Follow the instructions in the **Installing Environment Dependencies** section above.

Q: Why doesn't the app run correctly?
A: Ensure you've installed all the required libraries. If issues persist, consult the [FAQ section](#faq) or reach out to us for assistance.

We hope this user manual has been helpful! Enjoy using the Roll Dice App.