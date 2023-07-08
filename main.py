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
	pieceSquare = True
	for row in range(1,9):
		if row == 5:
			pieceSquare = False
		
		if pieceSquare == False:
			pieceSquare = True
		else:
			pieceSquare = False
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
