import tkinter as tk
import tkinter.font as tkFont
import threading
from tkinter import messagebox
from time import sleep

print("STAGE 2")
balldata = [0,10,10]

'''
Only run one method at a time.  They will otherwise conflict. 
'''

'''
def printit():

	#Change the 1.0 to reset the time interval that the function is called. 
	threading.Timer(1.0, printit).start()
	print ("Hello, World!")
	balldata[0] = balldata[0] + 1
	if balldata[0] % 2 == 0:
		canvas.create_oval(balldata[1],balldata[2],balldata[1] + 10,balldata[2] + 10, fill = "black",outline = "white")
	else:
		canvas.create_oval(balldata[1],balldata[2],balldata[1] + 10,balldata[2] + 10, fill = "white", outline = "white")

	print(balldata[0])
#'''

def printit():

	#Change the 1.0 to reset the time interval that the function is called. 
	threading.Timer(0.25, printit).start()
	print ("Hello, World!")
	
	
	canvas.create_oval(balldata[1],balldata[2],balldata[1] + 10,balldata[2] + 10, fill = "black",outline = "white")
	canvas.create_oval(balldata[1],balldata[2],balldata[1] + 10,balldata[2] + 10, fill = "white", outline = "white")
		
	canvas.create_oval(balldata[1],balldata[2],balldata[1] + 10,balldata[2] + 10, fill = "black",outline = "white")
	balldata[1] = balldata[1] + 1
	balldata[2] = balldata[2] + 1
	print(balldata[0])


root = tk.Tk()	
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()



printit()



root.mainloop();


