# FILENAME: app.py
# LANGUAGE: Python 3.x
'''
DOCSTRING:
This module imports and initializes the Dash library.
It sets up the necessary dependencies for running the app.
'''
import dash
from dash import dcc, html, callback_context
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
# Initialize the Dash app
app = Dash(__name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"])