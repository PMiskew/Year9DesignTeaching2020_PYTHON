import tkinter as tk
import tkinter.font as tkFont
import threading
from tkinter import messagebox
from time import sleep

print("STAGE 2")

#Binding Source Link
#https://www.python-course.eu/tkinter_events_binds.php
def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return

def background_task():

	xpos = 20
	ypos = 200
	while True:
		canvas.create_oval(xpos,ypos,xpos+20,ypos+20,fill = "black")
		
		canvas.create_oval(xpos,ypos,xpos+20,ypos+20,fill = "white")
		
		
		




def on_closing():
	if messagebox.askokcancel("Quit", "Do you want to quit?"):
		root.destroy()



root = tk.Tk()

#https://effbot.org/tkinterbook/canvas.htm
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

#Create image
#Task:  Using the documentation found at the below link
#	https://tkdocs.com/tutorial/canvas.html
# 	10 minutes - create a picture for me. 


canvas.create_rectangle(132,110,173,160, fill = "grey") #neck
canvas.create_oval(100,30, 200,130, fill = "grey") #head


fontStyle = tkFont.Font(family="Lucida Grande", size=50)
canvas.create_text(207, 100, text = "m", angle=270, font = fontStyle)

#use variables to change position quickly and maintain relationships
hx = 160
hy = 50
hr = 25
canvas.create_oval(hx,hy,hx+hr,hy+hr, fill = "white") #eye

canvas.create_oval(172,60,180,68,fill = "black") #pupil

#This creates a grid.  By using the loop we can shrink or exand the size
#Caution:	Remember loops take over the processor so while it is running
#			nothing else can happen.  This is often how a student first 
#			tries to create animations.  
#			Though this works the problem is nothign else can happen, such
#			as clicking
for i in range(0,40,3):

	canvas.create_line(0,0 + i,40,0 + i)
	canvas.create_line(0 + i,0,0 + i,40)


canvas.bind('<Motion>',motion) #bind a mouse motion listener

block_pos = canvas.coords(block.id)
console.log(blockpos);

#Creates Thread
#What is a thread?
#t = threading.Thread(target=background_task)
#t.start() #starts thread


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop();


