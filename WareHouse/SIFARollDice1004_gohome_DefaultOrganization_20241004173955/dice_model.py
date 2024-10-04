# FILENAME: dice_model.py
# LANGUAGE: Python 3.x
'''
DOCSTRING:
This module defines the business logic for rolling a dice.
It encapsulates the domain knowledge and provides a simple API for interacting with it.
'''
import dash
from dash.dependencies import Input, Output
import random
class DiceModel:
    def __init__(self):
        pass
    @staticmethod
    def roll_dice(sides):
        # Simulate rolling a dice by generating a random number between 1 and sides (inclusive)
        return random.randint(1, sides)
    def init(self, app):
        @app.callback(
            Output('result-graph', 'figure'),
            [Input('roll-button', 'n_clicks')],
            [State('dice-sides', 'value')]
        )
        def update_graph(n_clicks, sides):
            result = self.roll_dice(sides)
            # Update the graph with each new roll
            fig = {
                'data': [{'x': [1], 'y': [result]}],
                'layout': {'title': f'You rolled a {result}'}
            }
            return fig
    # Initialize the dice model
    def main(self):
        app = Dash(__name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"])
        self.init(app)
        app.run_server(debug=True)
# Initialize the dice model
dice_model = DiceModel()