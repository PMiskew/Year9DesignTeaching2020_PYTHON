from tkinter import *
from random import randint


def move_ball():
    deltax = 1 #andint(0,5)
    deltay = 1 #randint(0,5)
    canvas.move(ball1, deltax, deltay)
    root.after(50, move_ball)  # reschedule event in 2 seconds


# initialize root Window and canvas
root = Tk()
root.title("Balls")
root.resizable(False,False)
canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

ball1 = canvas.create_oval(10, 10, 20, 20, fill="red")


root.after(500, move_ball)
root.mainloop()

'''
# SITE: https://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop
from tkinter import *

root = Tk()

def task():
    print("hello")
    root.after(2000, task)  # reschedule event in 2 seconds

root.after(2000, task)
root.mainloop()
'''