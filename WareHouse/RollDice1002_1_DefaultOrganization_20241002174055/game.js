/**
 * Game component for rolling dice.
 */
import React from 'react';
class Game extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      diceCount: 1,
      sides: 6,
      diceConfig: [],
    };
    this.rollDice = this.rollDice.bind(this);
  }
  render() {
    return (
      <div>
        {this.renderDiceConfig()}
        <button onClick={this.rollDice}>Roll Dice</button>
        <label>Dice Count:</label>
        <input type="number" value={this.state.diceCount} onChange={(e) =>
          this.setState({ diceCount: parseInt(e.target.value, 10) })
        } />
      </div>
    );
  }
  renderDiceConfig() {
    return (
      <div>
        <label>Die Count:</label>
        <input type="number" value={this.state.diceCount} onChange={(e) =>
          this.setState({ diceCount: parseInt(e.target.value, 10) })
        } />
        <br />
        <label>Die Sides:</label>
        <select value={this.state.sides} onChange={(e) => (this.setState({ sides: e.target.value }))}
        >
          {Array.from(Array(6), (_, i) => (i + 1)).map((side) => (
            <option key={side} value={side}>
              {side}
            </option>
          ))}
        </select>
      </div>
    );
  }
  rollDice() {
    // API call to generate a new roll
    console.log(`Rolling ${this.state.diceCount}d${this.state.sides}`);
  }
}
export default Game;