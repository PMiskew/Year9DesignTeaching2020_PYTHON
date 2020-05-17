#This is our project 3 demo with no class structure
#
#	This project
#		- Refrehes our tkinter skills
#		- Reviews core ideas and terminology - IMPORTANT
#	
#

import tkinter as tk
print("STAGE 2 - PROJECT 3")
#Variables - Data 
#all you data must be lists or reference.



#Funcitons 
def check_login():
	print("Login Pressed")
	frame.pack_forget()
	frameMainScreen.pack()

def log_out():
	frameMainScreen.pack_forget()
	frame.pack()

#Set up our GUI
root = tk.Tk() #Construtor - A capitalized method is always a constructor


frame = tk.Frame(root, padx = 20, pady = 20, bg = "#4E4187", relief = tk.SUNKEN)
#Construct the objects/widget
lab1 = tk.Label(frame, text = "Enter First Name", bg = "#4E4187", fg = "#7DDE92")
lab2 = tk.Label(frame, text = "Enter Last Name", bg = "#4E4187", fg = "#7DDE92")
lab3 = tk.Label(frame, text = "Enter Access Code", bg = "#4E4187", fg = "#7DDE92")

text1 = tk.Text(frame, width = 30, height = 1, borderwidth = 2, relief= tk.GROOVE, fg = "#7DDE92")
text2 = tk.Text(frame, width = 30, height = 1, borderwidth = 2, relief= tk.GROOVE, fg = "#7DDE92")
text3 = tk.Text(frame, width = 30, height = 1, borderwidth = 2, relief= tk.GROOVE, fg = "#7DDE92")
btn = tk.Button(frame, text = "LOGIN", command = check_login)

#add it to the window
lab1.grid(row = 0, column = 0, sticky = "NESW")
lab2.grid(row = 1, column = 0, sticky = "NESW")
lab3.grid(row = 2, column = 0, sticky = "NESW")

text1.grid(row = 0, column = 1, columnspan = 2, sticky = "NESW")
text2.grid(row = 1, column = 1, columnspan = 2, sticky = "NESW")
text3.grid(row = 2, column = 1, columnspan = 2, sticky = "NESW")

btn.grid(row = 3, column = 1, sticky = "NESW")
frame.pack()


frameMainScreen = tk.Frame(root, width = 200, height = 200)
ms_btn = tk.Button(frameMainScreen, text="Log Out", command=log_out)
ms_btn.pack()

print("begin game")
root.mainloop()
print("end game")















