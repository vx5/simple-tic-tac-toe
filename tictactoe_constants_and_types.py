"""
Contains type classes used elsewhere in the project.
"""

from enum import Enum

# Types


class Player(Enum):
    """
    Represents one of the two Tic-Tac-Toe players.
    """
    PLAYER_1 = 'Player 1'
    PLAYER_2 = 'Player 2'


def switch_player(player: Player) -> Player:
    """
    Switch from one player to the other.
    """
    return Player.PLAYER_1 if player == Player.PLAYER_2 else Player.PLAYER_2


class PlayerToken(Enum):
    """
    Represents a valid board token which can be used by at most one player.
    """
    O = 'O'
    X = 'X'


class EntryResponse(Enum):
    """
    Represents a possible outcome after a user enters a location on the
    board to play.
    """
    ACCEPTED_ENTRY_GAME_NOT_OVER = "Entry accepted, game is not yet over"
    VICTORY = "Entry wins game"
    STALEMATE = "Entry accepted, game ends in stalemate"
    INVALID_ENTRY_SPOT_TAKEN = "Entry invalid because chosen location is already taken"
    INVALID_ENTRY_INVALID_LOCATION = "Entry invalid because chosen location is not on the board"


# CONSTANTS


# Overall number of rows
BOARD_DIMENSION = 3

# Sets characters used by each player
PLAYER_CHARS = {Player.PLAYER_1: PlayerToken.O, Player.PLAYER_2: PlayerToken.X}

# All messages to be printed to user
WELCOME_MSG = 'Welcome to Tic Tac Toe!'
BOARD_MSG = 'Here\'s the board:'
STALEMAGE_MSG = 'Game ends in stalemate!'
TAKEN_MSG = 'That position is taken -- please try again'
ENTER_MSG = 'Enter a position (# on board) to play:'
END_MSG = 'Thank you for playing!'
INVALID_IDX_MSG = f'Please enter an integer between 1 and {BOARD_DIMENSION ** 2}'


def turn_msg(cur_player: Player) -> str:
    return f"It is {cur_player.value}'s turn"


def victory_msg(cur_player: Player) -> str:
    return f"Player {cur_player.value} ({PLAYER_CHARS[cur_player]}) wins"


# Creates an Enum that represents each possible solution location on the board
sol_pos_enum_dict = {
    'RISING_DIAGONAL': "Diagonal from bottom left to top right",
    'FALLING_DIAGONAL': "Diagonal from top left to bottom right"
}
for i in range(BOARD_DIMENSION):
    sol_pos_enum_dict.update({f'ROW_{i}': f'Row_{i}'})
    sol_pos_enum_dict.update({f'COL_{i}': f'Col_{i}'})
SolutionPosition = Enum('SolutionPosition', sol_pos_enum_dict)
