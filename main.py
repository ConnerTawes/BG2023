from tkinter import *

# Creates Window
root = Tk()

# Sets Dimensions
root.geometry("800x600")

#Temp score
team1score = 1
team2score = 4

class Piece:

	def __init__(self, color):
		self.color = color

		# Changed rank = "Pawn" to self.rank = "Pawn" in the initilizer so that it can be referenced correctly
		self.rank = "Pawn"

	def funk(self):
  		print("|" + self.color, end="")


redPiece = Piece("Red")
blackPiece = Piece("Black")

board = [[blackPiece, None,       blackPiece, None,       blackPiece, None,       blackPiece, None],
		 [None,       blackPiece, None,       blackPiece, None,       blackPiece, None,       blackPiece],
		 [blackPiece, None,       blackPiece, None,       blackPiece, None,       blackPiece, None],
		 [None,       None,       None,       None,       None,       None,       None,       None],
		 [None,       None,       None,       None,       None,       None,       None,       None],
 		 [None,       redPiece,   None,       redPiece,   None,       redPiece,   None,       redPiece],
 		 [redPiece,   None,       redPiece,   None,       redPiece,   None,       redPiece,   None],
 		 [None,       redPiece,   None,       redPiece,   None,       redPiece,   None,       redPiece]]

for i in range (8):
	for j in range(8):
		if(board[i][j] == None):
			print("| ", end="")
		else:
			board[i][j].funk()
	print("")

def canMove(row, col, piece):
	if(piece.rank == "Pawn"):
		if(piece.color == "Black"):
			# Code for Black piece here
			if(row + 1 < 8):
				if(col - 1 >= 0 and col + 1 < 8):

					# If both down left and down right of black piece are empty
					if((board[row + 1][col - 1] == None) and (board[row + 1][col + 1] == None)):
						return [(row + 1, col - 1), (row + 1, col + 1)]

					#If left space is empty but right has a piece
					elif (board[row + 1][col - 1] == None):

						# Test for jump possibility
						if(board[row + 1][col + 1].color == "Red"):
							if(row + 2 < 8 and col + 2 < 8):
								if(board[row + 2][col + 2] == None):
									return [(row + 1, col - 1), (row + 2, col + 2)]

						# If cant jump, just return empty space
						return [row + 1, col - 1]

					#If right space is empty but left has a piece
					elif (board[row + 1][col + 1] == None):

						if(board[row + 1][col - 1].color == "Red"):
							if(row + 2 < 8 and col - 2 >= 0):
								if(board[row + 2][col - 2] == None):
									return [(row + 1, col - 1), (row + 2, col - 2)]

						return [(row + 1, col + 1)]
					else:
						# Test to see if either piece below black can be jumped


						###THIS IS WHERE I LEFT OFF


						# Might still be able to jump a piece
						return None

				elif (col - 1 >= 0):
					# Piece on right side of board
					if (board[row + 1][col - 1] ==  None):
						return [(row + 1, col - 1)]
					else:
						return None
				else:
					# Piece on left side of board
					if (board[row + 1][col + 1] ==  None):
						return [(row + 1, col + 1)]
					else:
						return None


		#else:
			# Code for Red piece here
	#else:
		# Code for king possibility here




def resetScore():
	"""
	This function is linked to the button 'Reset Score'
	Updates 'scorePad' to say 0 - 0
	No Parameters
	"""
	team1score = 0
	team2score = 0
	scorePad = Label(root, text=f"Score: {team1score} - {team2score}").grid(row=4, column = 9, columnspan=2)

def resetGame():
	"""
	WIP

	This function resets all piece positions to their original state
	"""
	return 0

def gameUpdate():
	"""
	This function builds the main game window; Board, Score Pad, Reset Score Button, Reset Game Button
	"""
	for widgets in root.winfo_children():
		widgets.destroy()
	for row in range(len(board)):
		for col in range(len(board[0])):
			if board[row][col] == blackPiece:
				b = Button(root, text=str(row) + str(col), bg="gray", width=8, height=4, borderwidth=2, command=lambda row=row,col=col:showMoves(row,col,blackPiece)).grid(row=row, column=col)
			elif board[row][col] == redPiece:
				b = Button(root, text=str(row) + str(col), bg="red", width=8, height=4, borderwidth=2, command=lambda row=row,col=col:showMoves(row,col,redPiece)).grid(row=row, column=col)
			elif board[row][col] == "Available":
				b = Button(root, text=str(row) + str(col), bg="blue", width=8, height=4, borderwidth=2).grid(row=row, column=col)
			else:
				b = Button(root, text=str(row) + str(col), state=DISABLED, width=8, height=4, borderwidth=2).grid(row=row, column=col)



	#Creates all off-board labels and buttons and assigns buttons to functions when clicked 
	scorePad = Label(root, text=f"Score: {team1score} - {team2score}")
	scorePad.grid(row=4, column = 9, columnspan=2)
	resetGameButton = Button(root, text="Reset Game")
	resetGameButton.grid(row=5, column=9)
	resetScoreButton = Button(root, text="Reset Score", command= lambda: [scorePad.grid_forget(), resetScore()])
	resetScoreButton.grid(row=5, column=10)

def showMoves(row, col, piece):
	"""
	This function will display the available moves of a clicked piece
	"""
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == "Available":
				board[i][j] = None

	
	for i in canMove(row, col, piece):
		print((i[0], i[1]))
		board[i[0]][i[1]] = "Available"

	gameUpdate()
		

	

def main():
	# Calling main window builder
	gameUpdate()

	

	# Activity loop
	root.mainloop()


if __name__ == "__main__":
	main()
