"""
Core logic for Tic-Tac-Toe game.
"""

from tictactoe_constants_and_types import *


class TicTacToeBoard:
    """
    Tic-Tac-Toe board that stores values, and allows get/set operations on the board
    using row and col numbers, stringifying of board.
    """

    def __init__(self):
        self.tokens_placed = 0
        self.board = [[None for _ in range(
            BOARD_DIMENSION)] for _ in range(BOARD_DIMENSION)]
        """
        Initializes each board position with a number (top row 1-2-3,
        next row 4-5-6, last 7-8-9 if BOARD_DIMENSION is 3).
        """
        for row in range(BOARD_DIMENSION):
            for col in range(BOARD_DIMENSION):
                self.board[row][col] = (row * BOARD_DIMENSION) + col + 1
        """
        Initialize dict that will track how many tokens each player has
        placed along possible solutions. Intentionally not using defaultdict
        to ensure that the dict rigidly expects a Player and a SolutionPosition.
        """
        self.player_and_solution_to_num_tokens = {}
        for player_token in list(PlayerToken):
            self.player_and_solution_to_num_tokens[player_token] = {}
            for solution_position in list(SolutionPosition):
                self.player_and_solution_to_num_tokens[player_token][solution_position] = 0

    def place_token(self, row: int, col: int, token: PlayerToken) -> EntryResponse:
        """
        Places given player token on the board in a position (if possible)
        and returns an EntryResponse depending on the outcome of attempting
        to place the token.

        INPUTS:
        row in inclusive range 0 to BOARD_DIMENSION (int) [row]
        col in inclusive range 0 to BOARD_DIMENSION (int) [col]
        token to be placed on the board (PlayerToken) [token]
        OUTPUT:
        info about attempt to place token in the given location (EntryResponse)
        """
        # Check whether given coordinates are on the board
        if not (0 <= row < BOARD_DIMENSION and 0 <= col < BOARD_DIMENSION):
            return EntryResponse.INVALID_ENTRY_INVALID_LOCATION
        # Check whether given coordinates are already taken by a player token
        if self.board[row][col] in [token.value for token in list(PlayerToken)]:
            return EntryResponse.INVALID_ENTRY_SPOT_TAKEN
        # Place token on the board at the specified location
        self.board[row][col] = token.value
        """
        Note which possible solutions this location helps -- if any solutions
        have been fulfilled, return victory response
        """
        # Check for the rows and cols along which this location lies
        row_solution_position = SolutionPosition(f'Row_{row}')
        self.player_and_solution_to_num_tokens[token][row_solution_position] += 1
        if self.player_and_solution_to_num_tokens[token][row_solution_position] == BOARD_DIMENSION:
            return EntryResponse.VICTORY
        col_solution_position = SolutionPosition(f'Col_{col}')
        self.player_and_solution_to_num_tokens[token][col_solution_position] += 1
        if self.player_and_solution_to_num_tokens[token][col_solution_position] == BOARD_DIMENSION:
            return EntryResponse.VICTORY
        # Check whether this location lies on either diagonal
        if row == col:
            self.player_and_solution_to_num_tokens[token][SolutionPosition.FALLING_DIAGONAL] += 1
            if self.player_and_solution_to_num_tokens[token][SolutionPosition.FALLING_DIAGONAL] == BOARD_DIMENSION:
                return EntryResponse.VICTORY
        if row + col + 1 == BOARD_DIMENSION:
            self.player_and_solution_to_num_tokens[token][SolutionPosition.RISING_DIAGONAL] += 1
            if self.player_and_solution_to_num_tokens[token][SolutionPosition.RISING_DIAGONAL] == BOARD_DIMENSION:
                return EntryResponse.VICTORY
        # Track that token was placed, check for potential stalemate
        self.tokens_placed += 1
        if self.tokens_placed == BOARD_DIMENSION ** 2:
            return EntryResponse.STALEMATE
        else:
            return EntryResponse.ACCEPTED_ENTRY_GAME_NOT_OVER

    def to_string(self) -> str:
        """
        Returns str representation of the current board contents.
        """
        final_str = ''
        for row in range(BOARD_DIMENSION):
            for col in range(BOARD_DIMENSION):
                final_str += str(self.board[row][col])
                # If this is not the last item in a row, add a divider
                if col < BOARD_DIMENSION - 1:
                    final_str += ' | '
            # If we are about to traverse a new row, add a row divider
            if row < BOARD_DIMENSION - 1:
                final_str += '\n' + ('--+-' * (BOARD_DIMENSION - 1)) + '-\n'
        return final_str


# User interaction section

# Print initial welcome message and initialize
print('\n' + WELCOME_MSG + '\n')
board = TicTacToeBoard()
cur_player = Player.PLAYER_1
while True:
    # Shows current board and asks for input
    print(BOARD_MSG + '\n')
    print(board.to_string())
    print('\n' + turn_msg(cur_player) + '\n')
    # Handle responses
    try:
        entry = int(input(ENTER_MSG))
        print(entry)
    except:
        # Default is an error value
        entry = (BOARD_DIMENSION ** 2) + 1
    # The user entry is 1-indexed, but the board is 0-indexed
    entry -= 1
    chosen_row = entry // BOARD_DIMENSION
    chosen_col = entry % BOARD_DIMENSION
    response = board.place_token(
        chosen_row, chosen_col, PLAYER_CHARS[cur_player])
    if response == EntryResponse.ACCEPTED_ENTRY_GAME_NOT_OVER:
        cur_player = switch_player(cur_player)
        continue
    if response == EntryResponse.INVALID_ENTRY_INVALID_LOCATION:
        print('\n' + INVALID_IDX_MSG + '\n')
        continue
    if response == EntryResponse.INVALID_ENTRY_SPOT_TAKEN:
        print('\n' + TAKEN_MSG + '\n')
        continue
    # If victory or stalemate, reprint the board and exit
    if response == EntryResponse.VICTORY:
        print(victory_msg(cur_player) + '\n')
    if response == EntryResponse.STALEMATE:
        print(STALEMAGE_MSG + '\n')
    print(board.to_string() + '\n')
    break

# Final message for end of game
print(END_MSG)
