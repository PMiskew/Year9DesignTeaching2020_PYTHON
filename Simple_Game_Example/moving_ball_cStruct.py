'''
This is pulled from the below site. 
https://stackoverflow.com/questions/25430786/moving-balls-in-tkinter-canvas

Note:   The StackOverflow site uses python2.  This means the tkinter import statement uses 
        capital T.  If you copy the code from the site and are using python 3 remember to
        make that change. 

Note:   This uses a class structure for the ball.  This is not something we are learning in 
        year 9 and it is important you don't just copy it and use it.  If you use this structure
        it please make a point of connecting with me. 


        


'''

from tkinter import *
from random import randint

class Ball:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="red")

    def move_ball(self):
        deltax = 1 #andint(0,5)
        deltay = 1 #randint(0,5)
        self.canvas.move(self.ball, deltax, deltay)
        self.canvas.after(50, self.move_ball)

# initialize root Window and canvas
root = Tk()
root.title("Balls")
root.resizable(False,False)
canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

# create two ball objects and animate them
ball1 = Ball(canvas, 10, 10, 30, 30)
ball2 = Ball(canvas, 60, 60, 80, 80)

ball1.move_ball()
ball2.move_ball()

root.mainloop()