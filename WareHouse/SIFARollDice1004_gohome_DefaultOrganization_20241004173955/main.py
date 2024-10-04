# FILENAME: main.py
# LANGUAGE: Python 3.x
'''
DOCSTRING:
This module serves as the entry point for the Roll Dice App.
It initializes the application, sets up the GUI, and begins the main event loop.
'''
from dash import Dash, dcc, html
import dice_model
def create_app():
    # Create a new instance of the Dash app
    app = Dash(__name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"])
    def render_layout():
        return [
            html.H1('Roll Dice App'),
            dcc.Input(id='dice-sides', type='number', placeholder='Enter number of sides', value=6),
            html.Button('Roll Dice', id='roll-button'),
            dcc.Graph(id='result-graph')
        ]
    # Set up the app layout
    app.layout = render_layout()
    # Initialize the dice model and setup callbacks
    return app
if __name__ == '__main__':
    import dash
    dash.__version__
    app = create_app()
    app.run_server(debug=True)