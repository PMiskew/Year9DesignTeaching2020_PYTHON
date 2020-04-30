from tkinter import * #you don't need the tk.
from random import randint


def move_ball():
	print("Ball Moving")
	deltax = 1
	deltay = 1
	canvas.move(ball1, deltax, deltay)
	canvas.move(ball2, -1*deltax, -1*deltay)
	root.after(50,move_ball)



root = Tk()
root.title("Moving Balls")
root.resizable(False,True);

#Notice that whenever I make an element
canvas = Canvas(root,width = 300, height = 300);
canvas.pack()

#Two things
# 1. I have to set up a timed interval to run a function
# 2. I have to tell the ball to move
ball1 = canvas.create_oval(10, 10, 20, 20, fill="red")
ball2 = canvas.create_oval(280, 280, 290, 290, fill="red")
print(ball1)
print(ball2)


#Create a function that is called on timed intervals
root.after(50,move_ball)
#What happens with the below line is it creates a game loop that runs and 
#waits for an event. 
root.mainloop();

print("DONE GAME")

