import tkinter as tk
from tkinter import *
from tkinter.ttk import *

master = tk.Tk(className="Tic Tac Toe")
master.geometry("300x300")

token="X"
board = [[],[],[]]
player1=True





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
    if board[r][c] == '_':
        return True
    return False


def updateBoard(player1, r, c):
	global board
	if player1:
		board[r][c] = "X"
	else:
		board[r][c] = "O"


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

def switchPlayers():
    global token,player1
    if player1:
        token="O"
    else:
        token="X"
    player1=not player1


def createUIBoard():
    btn_text.set("Game Started")
    for row in range(len(buttonArr)):
        for col in range(len(buttonArr[0])):
            buttonArr[row][col].config(bg='#f7e6fa')
    label_txt.set("Player Turn: "+token)
    resetBoard()

def playerButton(r,c):
    winner=checkWin(not player1)
    if (not winner and checkValid(r,c)):
        updateBoard(player1,r,c)
        buttonTextArr[r][c].set(token)
        switchPlayers()
        label_txt.set("Player Turn: "+token)
        if(checkWin(not player1) and (not player1)):
            label_txt.set("Player X won!!")
            btn_text.set("Game Ended")

            btn.config(bg='#e8fcfb')

        elif(checkWin(not player1)):
            label_txt.set("Player O won!!")
            btn.config(bg='#ffede3')
            btn_text.set("Game Ended")

    elif (not winner):
        print("Not a valid move")
    
    





#Setting up the UI of the gameboard
    
#Game Title
l1 = Label(master, text = "Python Tic-Tac-Toe")
l1.grid(row = 0, column = 1, sticky = W, pady = 2) 

#Arrays to store buttons for the game board
buttonArr=[[],[],[]]
buttonTextArr=[[],[],[]]

#Player Label
label_txt=tk.StringVar()
playerLabel=tk.Label(master,textvariable=label_txt)
playerLabel.grid(row=6,column=1,pady=2)


#Creates button grid along with the text variables within the buttons
for i in range(3):
        for j in range(3):
            buttonTextArr[i].append(tk.StringVar())
            buttonArr[i].append(tk.Button(master,textvariable=buttonTextArr[i][j],height=2,width=3,command= lambda x1=i, y1=j: playerButton(x1,y1)))
            buttonTextArr[i][j].set(" ")
            buttonArr[i][j].grid(row=i+1,column=j,pady=2)


#Start Button
btn_text = tk.StringVar()
btn = tk.Button(master, textvariable=btn_text, command=createUIBoard,height=2,width=15)
btn_text.set("Start")
btn.grid(row=5,column=1,pady=2)









master.mainloop()


