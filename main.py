from tkinter import *


root = Tk()

root.geometry("800x600")

team1score = 1
team2score = 4

def resetScore():
	team1score = 0
	team2score = 0
	scorePad = Label(root, text=f"Score: {team1score} - {team2score}").grid(row=4, column = 9, columnspan=2)

def resetGame():
	root.destroy()

def gameBuilder():
	pieceSquare = False
	for row in range(1,9):
		
		if pieceSquare:
			pieceSquare = False
		else:
			pieceSquare = True
		for col in range(1,9):
			if pieceSquare and row not in range(4,6):
				if row >= 6:
					Button(root, text=str(row) + str(col), bg="red", width=8, height=4, borderwidth=2).grid(row=row, column=col)
				else:
					Button(root, text=str(row) + str(col), bg="gray", width=8, height=4, borderwidth=2).grid(row=row, column=col)
				pieceSquare = False
			else:
				Button(root, text=str(row) + str(col), state=DISABLED, width=8, height=4, borderwidth=2).grid(row=row, column=col)
				pieceSquare = True

	scorePad = Label(root, text=f"Score: {team1score} - {team2score}")
	scorePad.grid(row=4, column = 9, columnspan=2)
	resetGameButton = Button(root, text="Reset Game")
	resetGameButton.grid(row=5, column=9)
	resetScoreButton = Button(root, text="Reset Score", command= lambda: [scorePad.grid_forget(), resetScore()])
	resetScoreButton.grid(row=5, column=10)
	buffer = Label(root, text=" "*25)
	buffer.grid(row=0)
gameBuilder()

root.mainloop()

class Piece:
	rank = "Pawn"
	def __init__(self, color):
		self.color = color

	def funk(self):
  		print("|" + self.color, end="")

redPiece = Piece("Red")
blackPiece = Piece("Black")

board = [[blackPiece, None, blackPiece, None, blackPiece, None, blackPiece, None],
		 [None, blackPiece, None, blackPiece, None, blackPiece, None, blackPiece],
		 [blackPiece, None, blackPiece, None, blackPiece, None, blackPiece, None],
		 [None, None, None, None, None, None, None, None],
		 [None, None, None, None, None, None, None, None],
 		 [None, redPiece, None, redPiece, None, redPiece, None, redPiece],
 		 [redPiece, None, redPiece, None, redPiece, None, redPiece, None],
 		 [None, redPiece, None, redPiece, None, redPiece, None, redPiece]]

for i in range (0, 8):
	for j in range(0,8):
		if(board[i][j] == None):
			print("| ", end="")
		else:
			board[i][j].funk()
	print("")

def CanMove(row, col, piece):
	if(piece.rank == "Pawn"):
		if(piece.color == "Black"):
			# Code for Black piece here
			if(row + 1 > 8):
				if(col - 1 >= 0 and col + 1 < 8):

					# If both down left and down right of black piece are empty
					if((board[row + 1][col - 1] == None) and (board[row + 1][col + 1] == None)):
						return [row + 1, col - 1, row + 1, col + 1]

					#If left space is empty but right has a piece
					elif (board[row + 1][col - 1] == None):

						# Test for jump possibility
						if(board[row + 1][col + 1].color == "Red"):
							if(row + 2 < 8 and col + 2 < 8):
								if(board[row + 2][col + 2] == None):
									return [row + 1, col - 1, row + 2, col + 2]

						# If cant jump, just return empty space
						return [row + 1, col - 1]

					#If right space is empty but left has a piece
					elif (board[row + 1][col + 1] == None):

						if(board[row + 1][col - 1].color == "Red"):
							if(row + 2 < 8 and col - 2 >= 0):
								if(board[row + 2][col - 2] == None):
									return [row + 1, col - 1, row + 2, col - 2]

						return [row + 1, col + 1]
					else:
						# Test to see if either piece below black can be jumped


						###THIS IS WHERE I LEFT OFF


						# Might still be able to jump a piece
						return [9]

				elif (col - 1 >= 0):
					# Piece on right side of board
					if (board[row + 1][col - 1] ==  None):
						return [row + 1, col - 1]
					else:
						return [9]
				else:
					# Piece on left side of board
					if (board[row + 1][col + 1] ==  None):
						return [row + 1, col + 1]
					else:
						return [9]


		#else:
			# Code for Red piece here
	#else:
		# Code for king possibility here
		return 0
