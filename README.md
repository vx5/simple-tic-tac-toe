# Simple CLI tic-tac-toe

## Introduction

This project is a simple 2-player tic-tac-toe game that is played from the command line:

![Sample gameplay](https://github.com/vx5/simple-tic-tac-toe/blob/main/images/screenshot.png)

## Key details

#### How to access

The game can be played from this project's root directory using the following terminal command:

```
python3 tictactoe.py
```

Users can then use integer inputs to select positions on the board, per the game's instructions.

#### Design details

The core logic of the game itself is in the game_logic module, while tictactoe.py handles user interactions. Both modules were designed with some degree of modularity, so that they can accommodate potential changes (e.g., different characters to represent players, different board sizes), with some modification.