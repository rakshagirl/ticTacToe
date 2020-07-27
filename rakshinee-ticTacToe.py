
name1 = ""
name2 = ""
board = [[]]

def resetBoard():
	global board
	board = [ ['_', '_', '_'],
 		['_', '_', '_'],
 		['_', '_', '_']]

def printBoard():
	global board
	print("  1 2 3")
	for i in range(1,4):
		print(str(i) + " " + " ".join(board[i-1]))


def checkValid(r, c):
	global board
	if r.isnumeric() and c.isnumeric():
		r = int(r)
		c = int(c)
		if r <=3 and r>=1 and c <=3 and c>=1:
			if board[r-1][c-1] == '_':
				return True
	return False


def updateBoard(player1, r, c):
	global board
	if player1:
		board[r-1][c-1] = "X"
	else:
		board[r-1][c-1] = "O"


def playerInput(player1):
	global name1, name2
	valid = False
	while not valid:
		if(player1):
			r = input(name1 + ", enter the row: ")
		else:
			r = input(name2 + ", enter the row: ")
		
		c = input("Enter the column: ")
		if checkValid(r, c):
			updateBoard(player1, int(r), int(c))
			valid = True
		else:
			print("You have entered an invalid row/column.")


def checkBounds(r, c):
	return r >= 0 and r<3 and c >=0 and c <3


def checkDirection(r, c, rInc, cInc, token):
	count = 0
	while checkBounds(r, c) and board[r][c] == token:
		count = count + 1
		r = r + rInc
		c = c + cInc
	return count == 3


def checkWin(player1):
	global board
	token = "X"
	if not player1:
		token = "O"
	for r in range(len(board)):
		for c in range(len(board[0])):
			row_inc = [-1, 0, 1, 1]
			col_inc = [0, 1, 1, -1]
			if board[r][c] == token:
				for i in range(len(row_inc)):
					if checkDirection(r, c, row_inc[i], col_inc[i], token):
						return True
	return False


def playGame():
	global name1, name2
	resetBoard()
	player1 = False
	winner = False 
	count = 0
	while not winner and count < 9:
		player1 = not player1
		printBoard()
		playerInput(player1)
		winner = checkWin(player1)
		count = count + 1
	if player1 and winner:
		print(name1 + " won!")
	elif winner:
		print(name2 + " won!")
	else:
		print("There is a tie!")

	printBoard()
	playAgain = input("Print y/n if you would like to play again!")
	return playAgain == "y"


# main gameplay
playAgain = True
name1 = input('Player 1, enter your name: ')
print('Hello, ' + name1)

name2 = input('Player 2, enter your name: ')
print("Hello, " + name2)
print(name1 + " you are X, and " + name2 + " you are O")

while (playAgain):
	playAgain = playGame()
print("Goodbye!")

