/**
 * Roll Dice App component.
 */
import React, { useState } from 'react';
import Game from './Game';
const RollDiceApp = () => {
  const [gameState, setGameState] = useState({
    diceCount: 1,
    sides: 6,
    diceConfig: [],
  });
  const rollDice = () => {
    // API call to generate a new roll
    console.log(`Rolling ${gameState.diceCount}d${gameState.sides}`);
  };
  return (
    <div>
      {this.renderDiceConfig()}
      <button onClick={rollDice}>Roll Dice</button>
      <label>Dice Count:</label>
      <input type="number" value={gameState.diceCount} onChange={(e) =>
        setGameState({ ...gameState, diceCount: parseInt(e.target.value, 10) })
      } />
    </div>
  );
};
const RenderDiceConfig = () => {
  const [gameState, setGameState] = useState({
    diceCount: 1,
    sides: 6,
    diceConfig: [],
  });
  return (
    <div>
      <label>Die Count:</label>
      <input type="number" value={gameState.diceCount} onChange={(e) =>
        setGameState({ ...gameState, diceCount: parseInt(e.target.value, 10) })
      } />
      <br />
      <label>Die Sides:</label>
      <select value={gameState.sides} onChange={(e) => (setGameState({ ...gameState, sides: e.target.value }))}
      >
        {Array.from(Array(6), (_, i) => (i + 1)).map((side) => (
          <option key={side} value={side}>
            {side}
          </option>
        ))}
      </select>
    </div>
  );
};
ReactDOM.render(<RollDiceApp />, document.getElementById('root'));