/**
 * Represents a single six-sided die.
 *
 * @description Rolls a die and returns the result.
 */
class Dice {
  constructor(config) {
    this.sides = config;
  }
  rollDie() {
    return Math.floor(Math.random() * this.sides) + 1;
  }
}
export default Dice;