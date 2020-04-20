import tkinter as tk
import tkinter.font as tkFont


#Binding Source Link
#https://www.python-course.eu/tkinter_events_binds.php
def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return

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

for i in range(0,40,3):

	canvas.create_line(0,0 + i,40,0 + i)
	canvas.create_line(0 + i,0,0 + i,40)


canvas.bind('<Motion>',motion) #bind a mouse motion listener







root.mainloop();