from tkinter import * #you don't need the tk.
from random import randint
import math

ball1data = [1,1]
ball2data = [-1,-1]

def move_ball():
	#print("Ball Moving")

	canvas.move(ball1, ball1data[0], ball1data[1])
	canvas.move(ball2, ball2data[0], ball2data[1])

	'''
	Year 10 Math: Geometry

	This is a long way to approach this problem, and really you want to find a 
	tool to abstract this. Abstraction is the art of hiding a process.  There is
	are functions out there that will do all of this for you and be more efficient 
	and effective.  L
	'''
	b1 = canvas.coords(ball1) #access coordinates of object on screen. 
	print(b1)
	b1x1 = b1[0]
	b1y1 = b1[1]
	b1x2 = b1[2]
	b1y2 = b1[3]
	#To find the center I use the midpoint formuala.  This works since it is a circle
	b1cx = (b1x1 + b1x2) / 2
	b1cy = (b1y1 + b1y2) / 2

	#b1r = math.sqrt((b1x2 - b1x1)**2 + (b1y2 - b1y1)**2)/2 #approximate
	#print(b1r)

	b1r = (b1y2 - b1y1)/2 #exact

	b2 = canvas.coords(ball2)
	b2x1 = b2[0]
	b2y1 = b2[1]
	b2x2 = b2[2]
	b2y2 = b2[3]
	b2cx = (b2x1 + b2x2) / 2
	b2cy = (b2y1 + b2y2) / 2

	#APPROXIMATE: Since a circle is drawing inside the square and I am using 
	#the corners the radius is slightly larger since it is based on the diagonal of
	#the square
	#b2r = math.sqrt((b2x2 - b2x1)**2 + (b2y2 - b2y1)**2)/2 #approximate
	#print(b2r)

	#EXACT: 
	b2r = (b2y2 - b2y1)/2 #exact
	print(b2r)




	#Intetrsection:
	#Step 1: Find distance between centers of circles
	d = math.sqrt((b2cx - b1cx)**2 + (b2cy - b2cy)**2)
	#Step 2: Check if distance between centers is larger than the sum of radius values
	if d < b2r + b1r:
		print("Intersecting")
		ball1data[0] = ball1data[0] * -1
		ball2data[0] = ball2data[0] * -1
		ball1data[1] = ball1data[1] * -1
		ball2data[1] = ball2data[1] * -1




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

