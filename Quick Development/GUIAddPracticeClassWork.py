import tkinter as tk
import random 
import os

#Create question log


#correct incorrect log


#files



nums = [3,4]
size = 36

def runMe():
	print("Running")

	result = int(entry.get())

	if (result == nums[0] + nums[1]):
		entry.config(bg ="white")

		print("Correct")
		#Generate two new numbers to display for the next question
		nums[0] = random.randint(0,10)
		nums[1] = random.randint(0,10)

		num1Label.config(text = nums[0])
		num2Label.config(text = nums[1])
		entry.delete(0, tk.END)

		randNum = random.randint(0,4)

		if (randNum == 0):
			os.system("say good job")
		elif (randNum == 1):
			os.system("say great work!")
		elif (randNum == 2):
			os.system("say spectacular")
		else:
			os.system("say keep going!")

	else:
		print("ERROR")
		entry.delete(0, tk.END)
		entry.config(bg = "red")




def say():
	print("Says the question")
	statement = str(nums[0]) + "+" + str(nums[1])+" = what"
	os.system("say "+statement)



root = tk.Tk()

num1Label = tk.Label(root, text = str(nums[0]), font = ("Helvetica",size))
num1Label.grid(row = 0, column = 0)

operationLabel = tk.Label(root, text = "+", font = ("Helvetica",size))
operationLabel.grid(row = 0, column = 1)

num2Label = tk.Label(root, text = str(nums[1]), font = ("Helvetica",size))
num2Label.grid(row = 0, column = 2)

equalLabel = tk.Label(root, text = "=", font = ("Helvetica",size))
equalLabel.grid(row = 0, column = 3)

entry = tk.Entry(root, width = 2, font = ("Helvetica",size))
entry.grid(row = 0, column = 4)

checkbtn = tk.Button(root, text = "CHECK", highlightbackground = "#3E4149", command = runMe, font = ("Helvetica",size))
checkbtn.grid(row = 1, column = 0, columnspan = 5, sticky = "nesw")

speakbtn = tk.Button(root, text = "SAY", highlightbackground = "#3E4149", command = say, font = ("Helvetica",size))
speakbtn.grid(row = 2, column = 0, columnspan = 5, sticky = "nesw")

output = tk.Text(root, height = 10, width = 30)
output.config(state = "disabled")
output.grid(row = 3, column = 0, columnspan = 5)






root.mainloop()
