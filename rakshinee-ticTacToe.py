
board = [ ['_', '_', '_'],
 		['_', '_', '_'],
 		['_', '_', '_']]

def printBoard():
	global board
	print("  1 2 3")
	for i in range(1,4):
		print(str(i) + " " + " ".join(board[i-1]))

def updateBoard(player1, r, c):
	global board
	if player1:
		board[r-1][c-1] = "X"
	else:
		board[r-1][c-1] = "O"


def playerInput(player1):
	if(player1):
		r = int(input(name1 + ", enter the row: "))
	else:
		r = int(input(name2 + ", enter the row: "))
	c = int(input("Enter the column: "))
	updateBoard(player1, r, c)



def playGame():
	name1 = input('Player 1, enter your name: ')
	print('Hello, ' + name1)

	name2 = input('Player 2, enter your name: ')
	print("Hello, " + name2)
	print(name1 + " you are X, and " + name2 + " you are O")


	player1 = False
	winner = False 
	count = 0
	while !winner and count < 9:
		player1 = !player1
		printBoard()

	# 	take player input 
	# 	check win
	# print winner
	# play again
	#count++




# main gamplay
	playAgain = True
	while (playAgain):
		playGame()
	print("Goodbye!")





