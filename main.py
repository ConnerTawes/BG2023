from tkinter import *
from PIL import ImageTk, Image

# Creates Window
root = Tk()

# Sets Dimensions
root.geometry("800x600")

# Opening Images
board_edge = Image.open("edge.png")

board_corner = Image.open("corner.png")

board_tile = Image.open("tile.png")

black_king = Image.open("black_king.png")
resize_black_king = black_king.resize((60,60))
black_king_picture = ImageTk.PhotoImage(resize_black_king)

black_pawn = Image.open("black_pawn.png")
resize_black_pawn = black_pawn.resize((60,60))
black_pawn_picture = ImageTk.PhotoImage(resize_black_pawn)

white_king = Image.open("white_king.png")
resize_white_king = white_king.resize((60,60))
white_king_picture = ImageTk.PhotoImage(resize_white_king)

white_pawn = Image.open("white_pawn.png")
resize_white_pawn = white_pawn.resize((60,60))
white_pawn_picture = ImageTk.PhotoImage(resize_white_pawn)



#Temp score
team0score = 1
team1score = 4

turn = -1
lastClicked = None

class Piece:

	def __init__(self, color):
		self.color = color

		# Changed rank = "Pawn" to self.rank = "Pawn" in the initilizer so that it can be referenced correctly
		self.rank = "Pawn"

	def prin(self):
  		print("|" + self.color + " " + self.rank, end="")

	def promote(self):
  		self.rank = "King"


redPiece = Piece("Red")
blackPiece = Piece("Black")
KB = Piece("Black")
KB.promote()
KR = Piece("Red")
KR.promote()

# board = [[blackPiece, None,       blackPiece, None,       blackPiece, None,       blackPiece, None],
# 		 [None,       blackPiece, None,       blackPiece, None,       blackPiece, None,       blackPiece],
# 		 [blackPiece, None,       blackPiece, None,       blackPiece, None,       blackPiece, None],
# 		 [None,       None,       None,       redPiece,       None,       None,       None,       None],
# 		 [None,       None,       None,       None,       blackPiece,       None,       None,       None],
#  		 [None,       redPiece,   None,       redPiece,   None,       redPiece,   None,       redPiece],
#  		 [redPiece,   None,       redPiece,   None,       redPiece,   None,       redPiece,   None],
#  		 [None,       redPiece,   None,       redPiece,   None,       redPiece,   None,       redPiece]]

board = [[None, None, None, None, None, None, None, None],
		[None, blackPiece, None, blackPiece, None, None, None, None],		 
		[None, None, KR, None, None, None, None, None],		
		[None, blackPiece, None, blackPiece, None, None, None, None],		 
		[None, None, None, None, redPiece, None, redPiece, None],		
		[None, None, None, None, None, KB, None, None], 		 
		[None, None, None, None, redPiece, None, redPiece, None],		
		[redPiece, None, None, None, None, None, None, None]]
		
for i in range (8):
	for j in range(8):
		if(board[i][j] == None):
			print("| ", end="")
		else:
			board[i][j].prin()
	print("")

def testBlackLeft(row, col):
	if(board[row + 1][col - 1].color == "Red"):
		if(row + 2 < 8 and col - 2 < 8):
			if(board[row + 2][col - 2] == None):
				return(row + 2, col - 2)

def testBlackRight(row, col):
	if(board[row + 1][col + 1].color == "Red"):
		if(row + 2 < 8 and col + 2 < 8):
			if(board[row + 2][col + 2] == None):
				return(row + 2, col + 2)

def testRedLeft(row, col):
	if(board[row - 1][col - 1].color == "Black"):
		if(row - 2 < 8 and col - 2 < 8):
			if(board[row - 2][col - 2] == None):
				return(row - 2, col - 2)

def testRedRight(row, col):
	if(board[row - 1][col + 1].color == "Black"):
		if(row - 2 < 8 and col + 2 < 8):
			if(board[row - 2][col + 2] == None):
				return(row - 2, col + 2)

def testBlackPawn(row, col, jumpReq):
	if(row + 1 < 8):
		if(col - 1 >= 0 and col + 1 < 8):

			# If both down left and down right of black piece are empty
			if((board[row + 1][col - 1] == None) and (board[row + 1][col + 1] == None) and not jumpReq):
				return [(row + 1, col - 1), (row + 1, col + 1)]

			#If left space is empty but right has a piece
			elif (board[row + 1][col - 1] == None):
				if(jumpReq):
					return [testBlackRight(row, col)]
				return [(row + 1, col - 1), testBlackRight(row, col)]

			#If right space is empty but left has a piece
			elif (board[row + 1][col + 1] == None):
				if(jumpReq):
					return[testBlackLeft(row, col)]
				return [testBlackLeft(row, col), (row + 1, col + 1)]

			# Test to see if either piece below black can be jumped
			else:
				return [testBlackLeft(row, col), testBlackRight(row, col)]

		elif (col - 1 >= 0):
			# Piece on right side of board
			if (board[row + 1][col - 1] ==  None):
				if(not jumpReq):
					return [(row + 1, col - 1)]
			else:
				return[testBlackLeft(row, col)]

		else:
			# Piece on left side of board
			if (board[row + 1][col + 1] ==  None):
				if(not jumpReq):
					return [(row + 1, col + 1)]
			else:
				return[testBlackRight(row, col)]

def testRedPawn(row, col, jumpReq):
	if(row - 1 >= 0):
		if(col - 1 >= 0 and col + 1 < 8):

			# If both up left and up right of red piece are empty
			if((board[row - 1][col - 1] == None) and (board[row - 1][col + 1] == None) and not jumpReq):
				return [(row - 1, col - 1), (row - 1, col + 1)]

			# Handles Double Jumping
			if(jumpReq):
				rtn = []
				if(board[row - 1][col - 1] is not None):
					rtn.append(testRedLeft(row, col))
				if(board[row - 1][col - 1] is not None):
					rtn.append(testRedRight(row, col))
				return rtn

			#If left space is empty but right has a piece
			elif (board[row - 1][col - 1] == None):
				if(jumpReq):
					return[testRedRight(row, col)]
				return [(row - 1, col - 1), testRedRight(row, col)]

			#If right space is empty but left has a piece
			elif (board[row - 1][col + 1] == None):
				if(jumpReq):
					return[testRedLeft(row, col)]
				return [testRedLeft(row, col), (row - 1, col + 1)]

			# Test to see if either piece above red can be jumped
			else:
				return [testRedLeft(row, col), testRedRight(row, col)]

		elif (col - 1 >= 0):
			# Piece on right side of board
			if (board[row - 1][col - 1] ==  None):
				if(not jumpReq):
					return [(row - 1, col - 1)]
			else:
				return[testRedLeft(row, col)]

		else:
			# Piece on left side of board
			if (board[row - 1][col + 1] ==  None):
				if(not jumpReq):
					return [(row - 1, col + 1)]
			else:
				return[testRedRight(row, col)]

def testKing(row, col, piece, jumpReq):
	rtn = []
	if(row - 1 >= 0):
		if(col - 1 >= 0):
			if((board[row - 1][col - 1] == None) and (not jumpReq)):
				rtn.append((row - 1), (col - 1))
			else:
				if(piece.color is not board[row - 1][col - 1].color):
					if(row - 2 >= 0 and col - 2 >= 0):
						if(board[row - 2][col - 2] is None):
							rtn.append((row - 2, col - 2))
		if(col + 1 < 8):
			if((board[row - 1][col + 1] == None) and (not jumpReq)):
				rtn.append((row - 1, col + 1))
			else:
				if(piece.color is not board[row - 1][col + 1].color):
					if(row - 2 >= 0 and col + 2 < 8):
						if(board[row - 2][col + 2] is None):
							rtn.append((row - 2, col + 2))
	if(row + 1 < 8):
		if(col - 1 >= 0):
			if((board[row + 1][col - 1] == None) and (not jumpReq)):
				rtn.append((row + 1, col - 1))
			else:
				if(piece.color is not board[row + 1][col - 1].color):
					if(row + 2 < 8 and col - 2 >= 0):
						if(board[row + 2][col - 2] is None):
							rtn.append((row + 2, col - 2))
		if(col + 1 < 8):
			if((board[row + 1][col + 1] == None) and (not jumpReq)):
				rtn.append((row + 1,col + 1))
			else:
				if(piece.color is not board[row + 1][col + 1].color):
					if(row + 2 < 8 and col + 2 < 8):
						if(board[row + 2][col + 2] is None):
							rtn.append((row + 2,col + 2))
	return rtn if rtn else None




def canMove(row, col, jumpReq):
	if board[row][col] is None:
		return None
	print(row, col, board[row][col].rank)
	if(board[row][col].rank == "Pawn"):
		if(board[row][col].color == "Black"):
			return testBlackPawn(row, col, jumpReq)
		else:
			return testRedPawn(row, col, jumpReq)

	# Piece must be a king
	print(testKing(row, col, board[row][col], jumpReq))
	return testKing(row, col, board[row][col], jumpReq)

def movePiece(row, col):
	global turn
	if turn == -1:
		board[row][col] = redPiece
		piece = redPiece
		turn = 1
	else:
		board[row][col] = blackPiece
		piece = blackPiece
		turn = -1

	board[lastClicked[0]][lastClicked[1]] = None

	# Removes a jumped piece
	if (lastClicked[0] - row) in (-2,2):
		jumpedRow = (row - lastClicked[0]) // 2
		jumpedCol = (col - lastClicked[1]) // 2
		board[row-jumpedRow][col-jumpedCol] = None

		# Test if piece can double jump
		moves = canMove(row, col, False)
		if moves is not None:
			for i in moves:
				if ((i[0] - row) % 2) == 0:
					turn *= -1
					canMove(row, col, True)


	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == "Available":
				board[i][j] = None

	gameUpdate()



def resetScore():
	"""
	This function is linked to the button 'Reset Score'
	Updates 'scorePad' to say 0 - 0
	No Parameters
	"""
	team0score = 0
	team1score = 0
	scorePad = Label(root, text=f"Score: {team0score} - {team1score}").grid(row=4, column = 9, columnspan=2)

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
			if board[row][col] == "Available":
				b = Button(root, text=str(row) + str(col), bg="blue", width=8, height=4, borderwidth=2, command=lambda row=row,col=col:movePiece(row,col)).grid(row=row, column=col)
			elif board[row][col] is not None and board[row][col].color == "Red":
				if turn == -1:
					b = Button(root, image = white_pawn_picture, borderwidth=2, command=lambda row=row,col=col:showMoves(row,col,redPiece)).grid(row=row, column=col)
				else:
					b = Button(root, image = white_pawn_picture, state=DISABLED, borderwidth=2, command=lambda row=row,col=col:showMoves(row,col,redPiece)).grid(row=row, column=col)
			elif board[row][col] is not None and board[row][col].color == "Black":
				if turn == 1:
					b = Button(root, image = black_pawn_picture, borderwidth=2, command=lambda row=row,col=col:showMoves(row,col,blackPiece)).grid(row=row, column=col)
				else:
					b = Button(root, image = black_pawn_picture, state=DISABLED, borderwidth=2, command=lambda row=row,col=col:showMoves(row,col,blackPiece)).grid(row=row, column=col)
			else:
				b = Button(root, text=str(row) + str(col), state=DISABLED, width=8, height=4, borderwidth=2).grid(row=row, column=col)



	#Creates all off-board labels and buttons and assigns buttons to functions when clicked 
	scorePad = Label(root, text=f"Score: {team0score} - {team1score}")
	scorePad.grid(row=4, column = 9, columnspan=2)
	resetGameButton = Button(root, text="Reset Game")
	resetGameButton.grid(row=5, column=9)
	resetScoreButton = Button(root, text="Reset Score", command= lambda: [scorePad.grid_forget(), resetScore()])
	resetScoreButton.grid(row=5, column=10)

def showMoves(row, col, piece):
	"""
	This function will display the available moves of a clicked piece
	"""
	global lastClicked

	lastClicked = (row, col)

	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == "Available":
				board[i][j] = None

	jumpReq = False
	# Check the board for forced jumps
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] is not None:
				if board[i][j].color == piece.color:
					for k in canMove(i, j, False):
						if k is not None:
							if ((k[0] - i) % 2 == 0):
								# A jump was found
								jumpReq = True

	moves = canMove(row, col, jumpReq)
	if moves is not None:
		for i in moves:
			if i is not None:
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