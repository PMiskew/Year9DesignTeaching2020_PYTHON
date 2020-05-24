#This is project 3 developed using a class structure
#	This project
#		- Gives an intrduction to class structure
#
#	Note:	This is really early to be learnign this and
#			it is very important that if you use this you
#			understand the larger concepts.  Not everyone
#			needs to do this!  There is lots of time to
#			learn this.   
#	
import tkinter as tk

class App():

	def __init__(self):
		
		self.root = tk.Tk() #Construtor - A capitalized method is always a constructor


		self.frame = tk.Frame(self.root, padx = 20, pady = 20, bg = "#4E4187", relief = tk.SUNKEN)
		#Construct the objects/widget
		self.lab1 = tk.Label(self.frame, text = "Enter First Name", bg = "#4E4187", fg = "#7DDE92")
		self.lab2 = tk.Label(self.frame, text = "Enter Last Name", bg = "#4E4187", fg = "#7DDE92")
		self.lab3 = tk.Label(self.frame, text = "Enter Access Code", bg = "#4E4187", fg = "#7DDE92")

		self.text1 = tk.Text(self.frame, width = 30, height = 1, borderwidth = 2, relief= tk.GROOVE, fg = "#7DDE92")
		self.text2 = tk.Text(self.frame, width = 30, height = 1, borderwidth = 2, relief= tk.GROOVE, fg = "#7DDE92")
		self.text3 = tk.Text(self.frame, width = 30, height = 1, borderwidth = 2, relief= tk.GROOVE, fg = "#7DDE92")
		self.btn = tk.Button(self.frame, text = "LOGIN")

		#add it to the window
		self.lab1.grid(row = 0, column = 0, sticky = "NESW")
		self.lab2.grid(row = 1, column = 0, sticky = "NESW")
		self.lab3.grid(row = 2, column = 0, sticky = "NESW")

		self.text1.grid(row = 0, column = 1, columnspan = 2, sticky = "NESW")
		self.text2.grid(row = 1, column = 1, columnspan = 2, sticky = "NESW")
		self.text3.grid(row = 2, column = 1, columnspan = 2, sticky = "NESW")

		self.btn.grid(row = 3, column = 1, sticky = "NESW")
		self.frame.pack()

		#self.root.mainloop()

	def doSomething(self):
		print("DOING")




l = App()



