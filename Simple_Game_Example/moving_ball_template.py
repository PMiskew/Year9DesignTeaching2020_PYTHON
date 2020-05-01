from tkinter import *
from random import randint


def move_ball():
	print("Moving")
	canvas.move(ball,1,1)

	root.after(50,move_ball)


#Building the screen
root = Tk() #constructs your root window
root.title("Ball Template")
root.resizable(False,False)

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

ball = canvas.create_oval(10,10,20,20, fill = "red") #ball
canvas.create_rectangle(3,3,300,300)


#Running things
root.after(50, move_ball)
root.mainloop() #enters a "game loop".
print("END PROGRAM")
