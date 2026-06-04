# Simple Naval Battle Game

A minimal, classic Battleship-style game implemented in Python with the pygame library. Place ships, take turns calling coordinates, and try to sink the opponent's fleet.
Made in Colégio Atlântico.

## About
This repository contains the game logic for a turn-based naval battle and some assets needed for the GUI. It is intended to be simple, readable, and easy to play. The game's messages are shown in Portuguese.

## How to play
- You place 3 ships on a 6x6 grid. Each ship takes a cell in the grid.
- When all of your ships are postioned, you can start guessing where the opponent (the computer with 3 randomised coordinates) has put its ships.
- Hits and misses are reported; ships are sunk when their only cell is hit.
- Each player has 25 attempts to sink the other player's ships.
- The winner is the player that destroyed all 3 ships first, or the one that sunk the most ships. A draw can happen.

## License
This project is released under the MIT License. See the LICENSE file for details.
