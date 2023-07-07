from tkinter import *
#import game.py
#import piece.py


root = Tk()

board = {}

team1score = 2
team2score = 3


pieceSquare = True

for row in range(8):
	if row == 5:
		pieceSquare = False
	
	if pieceSquare == False:
		pieceSquare = True
	else:
		pieceSquare = False
	for col in range(8):
		if pieceSquare and row not in range(3,5):
			if row >= 5:
				board[f'square{row}{col}'] = Button(root, text=str(row) + str(col), bg="red", width=6, height=3, borderwidth=2).grid(row=row, column=col)
			else:
				board[f'square{row}{col}'] = Button(root, text=str(row) + str(col), bg="gray", width=6, height=3, borderwidth=2).grid(row=row, column=col)
			pieceSquare = False
		else:
			board[f'square{row}{col}'] = Button(root, text=str(row) + str(col), state=DISABLED, width=6, height=3, borderwidth=2).grid(row=row, column=col)
			pieceSquare = True

	scorePad = Label(root, text=f"Score: {team1score} - {team2score}").grid(row=3, column = 8, columnspan=6)
	resetGameButton = Button(root, text="Reset Game").grid(row=4, column=8)
	resetScoreButton = Button(root, text="Reset Score").grid(row=4, column=9)


root.mainloop()