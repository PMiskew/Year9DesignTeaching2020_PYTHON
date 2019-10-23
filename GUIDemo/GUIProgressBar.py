import tkinter as tk

#stores the value in a list - This is because of some technical stuff
#A list is a collection of variables
#progress has 1 element, it has indexe 0
progress = [0]
'''
This program samples a health bar
'''
def addTask():
	print("task added")
	progress[0] = progress[0] + 1
	canvas.create_rectangle(0, 0, 10*progress[0],50, fill="blue")


def removeTask():
	print("task removed")
	progress[0] = progress[0] - 1
	canvas.create_rectangle(0,0,100,50, fill = "black")
	canvas.create_rectangle(0, 0, 10*progress[0],50, fill="blue")

root = tk.Tk()
'''
Stage 1:
Build a canvas and the knowing the number of pixles pick
a value that changes every time.
Stage 2:
Make it dynamic
'''

canvas = tk.Canvas(root, width = 100, height = 50, bg = "black")
canvas.grid(row = 0, column = 0, columnspan = 2)

btn1 = tk.Button(root, text = "A",command = addTask)
btn1.grid(row = 1, column = 0)
btn2 = tk.Button(root, text = "B",command = removeTask)
btn2.grid(row = 1, column = 1)




root.mainloop()
