from game_logic import printCurBoard, playMove

# Overall number of rows
numRows = 3
# Maps chars used by users to chars used in game_logic
# Update this to change the characters the user sees
charMap = {'O':'O', 'X':'X'}
keys = list(charMap.keys())
curPlayer = 0
# All messages to be printed to user
turnBreakLine = '============================'
welcomeMsg = 'Welcome to Tic Tac Toe!'
boardMsg = 'Here\'s the board:'
turnMsg = lambda curPlayer: f"It is player {curPlayer + 1} ({keys[curPlayer]})'s turn"
enterMsg = 'Enter a position (# on board) to play:'
victoryMsg = lambda curPlayer: f"Player {curPlayer + 1} ({keys[curPlayer]}) wins"
stalemateMsg = 'Game ends in stalemate!'
takenMsg = 'That position is taken -- please try again'
invalidIdxMsg = lambda numRows: f"Please enter an integer between 1 and {numRows ** 2}"
endMsg = 'Thank you for playing!'

# Receive player input on position
def solicit_board_input():
	while 1:
		try: entry = int(input(enterMsg))
		except: entry = 0
		print()
		# Checks for valid input
		response = playMove(charMap[keys[curPlayer]], entry)
		if response in ('success', 'victory', 'stalemate'): return response
		if response == 'taken': print(takenMsg + '\n')
		if response == 'invalid idx': print(invalidIdxMsg(numRows) + '\n')

# META: User interaction section
# Initial messages
print('\n' + welcomeMsg + '\n')
# REPL loop for processing user input
while 1:
	# Shows current board and asks for input
	print(boardMsg + '\n')
	printCurBoard()
	print('\n' + turnMsg(curPlayer) + '\n')
	# Handle responses
	response = solicit_board_input()
	if response == 'success': 
		curPlayer = (curPlayer + 1) % 2
		continue
	if response == 'victory': print(victoryMsg(curPlayer) + '\n')
	if response == 'stalemate': print(stalemateMsg + '\n')
	printCurBoard()
	print()
	break

# Final game-ending message
print(endMsg + '\n')