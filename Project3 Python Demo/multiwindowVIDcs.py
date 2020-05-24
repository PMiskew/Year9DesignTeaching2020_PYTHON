'''


XXXXXXX
X     X
X  1  X  1 -- > 2
X     X  1 -- > 3
X     X
XXXXXXX



XXXXXXX
X     X
X  2  X 2 --> 3
X     X
X     X
XXXXXXX



XXXXXXX
X     X  3 --> 1
X  3  X
X     X
X     X
XXXXXXX



'''

import tkinter as tk

class App():


	#Attributes - Fields
	#Constructors
	def __init__(self):

		self.root = tk.Tk()

		self.frame1 = tk.Frame(self.root, bg = "red")
		self.frame2 = tk.Frame(self.root, bg = "blue")
		self.frame3 = tk.Frame(self.root, bg = "green")

		self.lab1f1 = tk.Label(self.frame1, text = "Label 1 in Frame 1")
		self.lab1f2 = tk.Label(self.frame2, text = "Label 1 in Frame 2")
		self.lab1f3 = tk.Label(self.frame3, text = "Label 1 in Frame 3")

		self.btn1to3 = tk.Button(self.frame1, text = "1 to 3", command = self.fnc1to3)
		self.btn1to2 = tk.Button(self.frame1, text = "1 to 2", command = self.fnc1to2)

		self.btn2to3 = tk.Button(self.frame2, text = "2 to 3", command = self.fnc2to3)

		self.btn3to1 = tk.Button(self.frame3, text = "3 to 1", command = self.fnc3to1)

		#frame 1
		self.lab1f1.pack()
		self.btn1to3.pack()
		self.btn1to2.pack()

		#frame 2
		self.lab1f2.pack()
		self.btn2to3.pack()

		#frame 3
		self.lab1f3.pack()
		self.btn3to1.pack()




		self.frame1.pack()
		self.root.mainloop()

	#Behaviours - Methods
	def fnc1to2(self):
		print("1 to 2")
		self.frame1.pack_forget()
		self.frame2.pack()

	def fnc1to3(self):
		print("1 to 3")
		self.frame1.pack_forget()
		self.frame3.pack()

	def fnc2to3(self):
		print("2 to 3")
		self.frame2.pack_forget()
		self.frame3.pack()

	def fnc3to1(self):
		print("3 to 1")
		self.frame3.pack_forget()
		self.frame1.pack()




a = App()




















