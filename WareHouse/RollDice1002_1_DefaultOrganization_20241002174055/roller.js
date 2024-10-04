/**
 * Handles the logic for rolling multiple dice.
 *
 * @description Manages the roller's configuration and rolls dice based on it.
 */
import React from 'react';
class Roller extends React.Component {
  constructor(props) {
    super(props);
    this.dice = [];
  }
  rollMultipleDice() {
    const result = this.dice.map((die) => die.rollDie());
    console.log(`Rolling ${this.dice.length}d${this.sides}: ${result}`);
  }
  setConfig(config) {
    this.dice = config.map((die) => new Dice(die));
  }
}
export default Roller;