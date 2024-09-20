# Card Game README

## Overview

This Python program implements a multiplayer card game involving four players. The objective of the game is to win rounds by playing higher-ranked cards based on the rules of the game. The game is played over multiple rounds, with players earning points based on their performance.

## Features

- Supports up to 4 players.
- Random card shuffling and dealing.
- Players can call for a specific number of wins.
- Tracks points over multiple games.
- Displays the current status and cards of each player.

## Installation

1. Ensure you have Python 3.x installed on your machine.
2. Clone or download the repository to your local machine.
3. Navigate to the project directory.
4. Run the program using the command:

   ```bash
   python call_break.py
   ```

## Usage

1. **Player Setup**: When prompted, enter the names of the four players.
2. **Game Flow**:
   - The game consists of multiple rounds.
   - Players will be prompted to call the number of wins they expect to achieve.
   - Players take turns playing cards according to the rules.
   - Points are awarded based on performance, and overall scores are maintained.
3. **End of Game**: After a predetermined number of games (4), the program will declare an overall winner based on the points scored across all games.

## Gameplay Rules

- Each player is dealt a hand of cards, and the game proceeds in rounds.
- Players can only play a card that matches the suit of the leading card or a trump card (♠).
- The winner of each round is determined based on card rank.
- Points are awarded based on the number of rounds won compared to the player's initial call.

## Code Structure

- **Classes**:
  - `Card`: Represents a playing card with a rank and suit.
  - `Deck`: Represents a deck of cards with functionalities to shuffle and draw.
  - `Player`: Represents a player with a hand of cards and points.
  
- **Functions**:
  - `loading()`: Displays a loading animation during the game.
  
## Contributions

Feel free to contribute to this project by suggesting improvements or reporting issues.

## License

This project is licensed under the MIT License.
