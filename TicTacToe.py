#!/usr/bin/python

# Initializes board variable
board = [" "] * 9
# Initializes instruction board
instruct_board = []
for i in range(1, 10):
	instruct_board.append(i)
# Store player's turn (even is player 1, odd is player 2)
turn = 0

# Prints Tic Tac Toe board based on list of 9 characters
def print_board(board_chars):
	str_board_chars = map(str, board_chars)
	print(str_board_chars[0] + " | " + str_board_chars[1] + " | " + str_board_chars[2])
	print("--+---+--")
	print(str_board_chars[3] + " | " + str_board_chars[4] + " | " + str_board_chars[5])
	print("--+---+--")
	print(str_board_chars[6] + " | " + str_board_chars[7] + " | " + str_board_chars[8])

# Evaluates board to determine whether either player has won
def eval_board(board_chars):
	char = board[0]
	# Check for starts in top-left
	if char != " ":
		if char == board[1] == board[2]:
			return char
		elif char == board[3] == board[6]:
			return char
		elif char == board[4] == board[8]:
			return char
	# Check for starts in top-middle
	char = board[1]
	if char != " ":
		if char == board[4] == board[7]:
			return char
	# Check for starts in top-right
	char = board[2]
	if char != " ":
		if char == board[4] == board[6]:
			return char
		elif char == board[5] == board[8]:
			return char
	# Check for starts in mid-left
	char = board[3]
	if char != " ":
		if char == board[4] == board[5]:
			return char
	# Check for starts in bottom-left
	char = board[6]
	if char != " ":
		if char == board[7] == board[8]:
			return char
	# Check for stalemate
	populated = True
	for i in range(0, 9):
		if board[i] == " ":
			populated = False
			break
	if populated:
		return "Stalemate"
	return ""

# Receive player input on position
def solicit_board_input(char):
	while 1:
		try: 
			entry = int(input("Enter a position to play:"))
		except (NameError, SyntaxError):
			entry = -1
		# Checks for valid input
		if entry < 1 or entry > 9:
			print("\nERROR: Please enter a value between 1 and 9\n")
		else:
			# Checks for input on new space
			if board[entry] != " ":
				print("\nERROR: space " + str(entry) + " is already taken by " + board[entry] + "\n")
			else:
				board[entry - 1] = char
				print("\n")
				return

# Populates standard break
def show_break():
	print("\n============================\n")

# User interaction section
print("Welcome to Tic Tac Toe!\n")
print("Use the below key for selecting positions:\n")
print_board(instruct_board)
show_break()
# REPL loop for processing user input
while 1:
	# Shows current board and asks for input
	print("Here's the board:\n")
	print_board(board)
	show_break();
	# Check if game is over
	status = eval_board(board)
	if status == "Stalemate":
		print("Game ends in stalemate!\n")
		break
	elif status == "X":
		print("Player 1 wins (X)!\n")
		break
	elif status == "O":
		print("Player 2 wins (O)!\n")
		break
	# Offer prompts by player, updates turns
	current_char = "X"
	player = "1"
	if turn % 2 == 1:
		current_char = "O"
		player = "2"
	print("It is Player " + player + "'s turn (" + current_char + ")\n");
	turn += 1
	# Receives user input
	solicit_board_input(current_char)
	
# Final game-ending message
print("Thank you for playing!\n")
