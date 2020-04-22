import tkinter as tk

def motion(event):
	print("Mouse position: (%s %s)" % (event.x,event.y))
	return


print("START");
root = tk.Tk()


#Assignment statement
#Using the Canvas constructor to create a canvas object

canvas = tk.Canvas(root, width = 300, height = 300)
canvas.pack()

canvas.create_rectangle(132,110,173,160, fill = "grey")
canvas.create_oval(100,30, 200,130, fill = "grey")

#loop is really useful to draw some pattern. 
#If you use a delay you can make it look like something is moving across
#the screen
for i in range(0,40,3):

	canvas.create_line(0,0 + i,40,0 + i)
	canvas.create_line(0 + i,0,0 + i,40)



canvas.bind('<Motion>',motion) #bind a mouse motion listener
#mainloop is an instance method that starts up the program in
#an infinite loop and waits for something to happen. 
root.mainloop();

print("END")