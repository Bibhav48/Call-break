# Call Break - A Python Game

This repository contains the Python code for a game called Call Break.

## How to Play

Call Break is a popular trick-taking card game played in South Asia. This implementation is for four players.

Here's a basic overview of the gameplay:

1. **Dealing:** A standard deck of 52 cards is used. Each player receives 13 cards dealt one at a time.
2. **Calling:** Players take turns calling the number of tricks they believe they can win in the round. The player who calls the highest number gets to choose the trump suit (Spade by default).
3. **Playing the Round:** Players take turns playing a card, following suit if possible. If unable to follow suit, players can play any card, including a trump card. The highest card of the leading suit or the highest trump card wins the trick.
4. **Scoring:** At the end of the round, players who win the number of tricks they called receive points equal to their call. Players who fail to meet their call lose points equal to their call.

## Running the Game

1. Clone this repository or download the code.
2. Install Python 3 on your system if you haven't already.
3. Open a terminal or command prompt and navigate to the directory containing the code.
4. Run the following command to start the game:

```bash
python main.py
```

## Gameplay Features

* Player names can be entered during setup.
* Points are tracked throughout the game for each player.
* Winners for each round and overall game are displayed.

## Code Structure

The code is organized into several classes:

* `Card`: Represents a single playing card with suit and rank.
* `Deck`: Manages a deck of cards, including shuffling and dealing.
* `Player`: Represents a player in the game, holding cards and keeping track of points.

The main logic resides in the `main.py` file, handling game setup, rounds, scoring, and overall winner determination.

### Additional Notes

* This is a basic implementation of Call Break. More advanced features can be added, such as bidding for trump suit and side bets.
* The code relies on the `os` and `time` modules for system interactions and delays, respectively.

Feel free to modify and extend the code to create your own customized Call Break experience!
