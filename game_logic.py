# Constants
# If numRows > 3, output printing should be adjusted, to ensure board correctly prints
# double-digit numbers (for numRows = 3, numbers on boards are 1-9)
numRows = 3
# Characters used by players
oneChar, twoChar = 'O', 'X'
# State variables for TicTacToe
# Storage of current board
curBoard = [idx + 1 for idx in range(numRows ** 2)]
# Count moves made to check for stalemate
movesMade = 0
# Storage of possible solutions
solsCount = {oneChar: {}, twoChar: {}}

# INPUTS: None
# OUTPUT: None
# ACTION: Solutions dict is initialized with all possible solutions and count of chars toward winning
def initSols():
	for playerChar in solsCount:
		# Initialize row and column solutions
		for idx in range(numRows):
			solsCount[playerChar]['R' + str(idx)] = 0
			solsCount[playerChar]['C' + str(idx)] = 0
		# Initialize diagonal solutions, pos/neg diag refer to slopes of diagonals
		solsCount[playerChar]['posDiag'] = 0
		solsCount[playerChar]['negDiag'] = 0

# INPUTS: None
# OUTPUT: None
# ACTION: Current board is printed out
def printCurBoard():
	for elem in range(numRows ** 2):
		# Prints element
		print(curBoard[elem], end = '')
		# Either prints for newline, or divider
		if (elem + 1) % numRows == 0 and (elem + 1) // numRows < numRows: 
			print()
			for _ in range(numRows - 1): print('--+-', end = '')
			print('-')
		elif (elem + 1) % numRows != 0: print(' | ', end = '')
	# Final newline
	print()

# INPUTS:
# - Token with length=1 representing player (str) [playerChar]
# - index player wishes to play (int) [idx]
# OUTPUT:
# - 'victory' if move results in player winning
# - 'stalemate' if move results in stalemate
# - 'success' if move made successfully
# - 'taken' if position is already taken
# - 'invalid idx' if idx indicated is not valid
# - 'invalid player' if playerChar indicated is not valid
def playMove(playerChar, idx):
	global movesMade
	# Check for playerChar
	if playerChar not in (oneChar, twoChar): return 'invalid player'
	# Adjust index from 1-idx (shown to user) to 0-idx (used for accessing state)
	idx -= 1
	# Check for valid idx or taken position
	if type(idx) is not int or not (0 <= idx < numRows ** 2): return 'invalid idx'
	if type(curBoard[idx]) is not int: return 'taken'
	# Place character on board, increment movesMade
	curBoard[idx] = playerChar
	movesMade += 1
	if movesMade == numRows ** 2: return 'stalemate'
	# Update state variables, check for victory case
	row, col = str(idx // numRows), str(idx % numRows)
	# Check if there is victory on current row and col
	solsCount[playerChar]['R' + row] += 1
	if solsCount[playerChar]['R' + row] == numRows: return 'victory'
	solsCount[playerChar]['C' + col] += 1
	if solsCount[playerChar]['C' + col] == numRows: return 'victory'
	# Check if there is victory on either diagonal
	row, col = int(row), int(col)
	if row + col == numRows - 1:
		solsCount[playerChar]['posDiag'] += 1
		if solsCount[playerChar]['posDiag'] == numRows: return 'victory'
	if row == col:
		solsCount[playerChar]['negDiag'] += 1
		if solsCount[playerChar]['negDiag'] == numRows: return 'victory'
	# Else simply return success
	return 'success'

# Initialization
initSols()