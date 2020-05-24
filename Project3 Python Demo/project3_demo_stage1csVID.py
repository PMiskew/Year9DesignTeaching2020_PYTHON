#A class is a blueprint that is used to make objects
import tkinter as tk

class App():

	#Fields - Attributes
	#Constructors - Special methods called when we first create an instance
	def __init__(self):
		print("Builing App")
		#Build my GUI

		self.root = tk.Tk() #Capitalize methods are constructors

		self.frame = tk.Frame(self.root, padx = 20, pady = 20, bg = "#4E4187", relief = tk.SUNKEN)

		self.lab1 = tk.Label(self.frame, text = "Enter First Name", bg = "#4E4187", fg = "#7DDE92")
		self.lab2 = tk.Label(self.frame, text = "Enter Last Name", bg = "#4E4187", fg = "#7DDE92")
		self.lab3 = tk.Label(self.frame, text = "Enter Access Code", bg = "#4E4187", fg = "#7DDE92")

		self.text1 = tk.Text(self.frame, width = 30, height = 1, borderwidth = 2, relief= tk.GROOVE, fg = "#7DDE92")
		self.text2 = tk.Text(self.frame, width = 30, height = 1, borderwidth = 2, relief= tk.GROOVE, fg = "#7DDE92")
		self.text3 = tk.Text(self.frame, width = 30, height = 1, borderwidth = 2, relief= tk.GROOVE, fg = "#7DDE92")
		
		self.btn = tk.Button(self.frame, text = "LOGIN")

		self.lab1.grid(row = 0, column = 0)
		self.lab2.grid(row = 1, column = 0)
		self.lab3.grid(row = 2, column = 0)

		self.text1.grid(row = 0, column = 1, columnspan = 2)
		self.text2.grid(row = 1, column = 1, columnspan = 2)
		self.text3.grid(row = 2, column = 1, columnspan = 2)

		self.btn.grid(row = 3, column = 1, sticky = "NESW")

		self.frame.pack()
		self.root.mainloop()



	#Method - Behaviours

a = App() #Create an app object and store the reference in a
