import tkinter as tk
import tkinter.font as tkFont


#Binding Source Link
#https://www.python-course.eu/tkinter_events_binds.php

def motion(event):
	print("Mouse position: (%s %s)" % (event.x, event.y))

def click(event):

	print("click")

	x = event.x
	y = event.y

	if not(100 < x < 200 and 100 < y < 200):
		print("outside")
		canvas.create_oval(x,y,x+5,y+5,fill = "blue")

def drawcheckerboard():
	
	#Creates 10 by 10 checkerboard:
	canvas.create_rectangle(100,100,200,200);

	ypos = 100;

	for j in range(0,5,1):

		#The inside loop fills in an entire row. 
		for i in range(100,200,20):

			#The two rows are offset, we only draw the black squares. 
			canvas.create_rectangle(i,ypos,i + 10,ypos + 10,fill="black") #first row
			canvas.create_rectangle(i+10,ypos + 10,i + 20,ypos + 20,fill="black") #second row
		
		#shifts the drawing position down 20 pixles. This is two rows since each row is 10 pixles.
		ypos = ypos + 20; 



root = tk.Tk()

#https://effbot.org/tkinterbook/canvas.htm
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()




#The outside loop is for the rows.  It completes two rows at a time to account for 
#the alternation between white and black first square. 

'''
j = 0
	i = 100 RUN LOOP CODE
	B
	 B
	i = 120 RUN LOOP CODE
	B B
	 B B
	i = 140 RUN LOOP CODE
	B B B
	 B B B
	i = 160 RUN LOOP CODE
    B B B B
	 B B B B
	i = 180 RUN LOOP CODE
	B B B B B
	 B B B B B
	i = 200 EXIT LOOP
ypos = ypos + 20
j = 1

i = 100 RUN LOOP CODE
	B B B B B
	 B B B B B
	B
	 B
	i = 120 RUN LOOP CODE
	B B B B B
	 B B B B B
	B B
	 B B
	i = 140 RUN LOOP CODE
	B B B B B
	 B B B B B
	B B B
	 B B B
	i = 160 RUN LOOP CODE
  	B B B B B
	 B B B B B
	B B B B
	 B B B B
	i = 180 RUN LOOP CODE
	B B B B B
	 B B B B B
	B B B B B
	 B B B B B
	i = 200 EXIT LOOP
'''
drawcheckerboard()
#drawcheckerboard(100)

canvas.bind('<Motion>',motion) #bind a mouse motion listener

canvas.bind('<Button-1>',click) #bind a mouse motion listener



root.mainloop();


