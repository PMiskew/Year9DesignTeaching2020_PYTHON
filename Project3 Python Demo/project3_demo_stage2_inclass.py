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
fnames = ["fname1","fname2"]
lnames = ["lname1","lname2"]
acodes = ["0","1"]


#Funcitons 
def check_login():
	print("check Login")

	check = False #You are not verified
	#Write a loop to go through lists and check values
	#THIS IS CODING BAT
	
	fn = text1.get()
	ln = text2.get()
	ac = text3.get()

	print(fn)
	print(ln)
	print(ac)

	for i in range (0,len(fnames),1):
		if (fn == fnames[i] and ln == lnames[i] and ac == acodes[i]):
			print("*******")
			check = True


	print(check)
	if (check == True):
		frame.pack_forget()
		frameMainScreen.pack()

def logout():
	frameMainScreen.pack_forget()
	frame.pack()

#Set up our GUI
root = tk.Tk() #Construtor - A capitalized method is always a constructor

root.geometry("400x200")
#************FRAME 1*************
frame = tk.Frame(root, padx = 20, pady = 20, bg = "#4E4187", relief = tk.SUNKEN)
#Construct the objects/widget
lab1 = tk.Label(frame, text = "Enter First Name", bg = "#4E4187", fg = "#7DDE92")
lab2 = tk.Label(frame, text = "Enter Last Name", bg = "#4E4187", fg = "#7DDE92")
lab3 = tk.Label(frame, text = "Enter Access Code", bg = "#4E4187", fg = "#7DDE92")

text1 = tk.Entry(frame, width = 30,borderwidth = 2, relief= tk.GROOVE, fg = "#7DDE92")
text2 = tk.Entry(frame, width = 30, borderwidth = 2, relief= tk.GROOVE, fg = "#7DDE92")
text3 = tk.Entry(frame, width = 30, borderwidth = 2, relief= tk.GROOVE, fg = "#7DDE92")
btn = tk.Button(frame, text = "LOGIN", command = check_login)

#add it to the window
lab1.grid(row = 0, column = 0, sticky = "NESW")
lab2.grid(row = 1, column = 0, sticky = "NESW")
lab3.grid(row = 2, column = 0, sticky = "NESW")

text1.grid(row = 0, column = 1, columnspan = 2, sticky = "NESW")
text2.grid(row = 1, column = 1, columnspan = 2, sticky = "NESW")
text3.grid(row = 2, column = 1, columnspan = 2, sticky = "NESW")

btn.grid(row = 3, column = 1, sticky = "NESW")

#***********FRAME 2**************
frameMainScreen = tk.Frame(root)
logout_btn = tk.Button(frameMainScreen, text = "Logout",  command = logout)
logout_btn.grid(row = 0, column = 0)



frame.pack()



print("begin game")
root.mainloop()
print("end game")















