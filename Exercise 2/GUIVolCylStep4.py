import math
import tkinter as tk


'''
This function takes two numeric values and calculates 
the volume of a cylinder.  It returns the volume.  If
the passed parameters are invalid it returns -1
'''
def calcVolumeCylinder(radius, height):
	
	if radius >= 0 and height >= 0:
		volume = math.pi * pow(radius,2) * height
		volume = round(volume, 2)
		return volume
	else:
		return -1

def runMe():
	print("RUNNING")
	r = radiusEntry.get() #gets the value from the entry as a String
	
	try:
		r = float(r) #cast r to float
	except:
		r = -1


	radiusEntry.delete(0, tk.END)

	h = heightEntry.get() #gets value and stores in r
	
	try:
		h = float(h) #casts r to float
	except:
		h = -1

	heightEntry.delete(0,tk.END) #deltes content of entry tk.END gets last char

	

	volume = calcVolumeCylinder(r,h)
	print(volume)

	if volume != -1:
		output.config(state = "normal")
		output.delete("1.0",tk.END) #delete everything
		result = "\n\n\tr\t= "+str(r)+" units\n\th\t= "+str(h)+" units\n\tvolume\t= "+str(volume)+" units\u00B3"
		output.insert(tk.END,result)
		output.config(state = "disabled")	

		file.write(str(r)+"\n")
		file.write(str(h)+"\n")
		file.write(str(volume)+"\n")
	else:
		output.config(state = "normal")
		output.delete("1.0",tk.END) #delete everything
		output.insert(tk.END,"BAD INPUT")
		output.config(state = "disabled")	

def checkSelect():
	state = var.get()

	if state == 1:
		print("High Contrast")
		radiusLabel.config(fg = "white", bg = "black")
		heightLabel.config(fg = "white", bg = "black")
		radiusEntry.config(fg = "white", bg = "black")
		heightEntry.config(fg = "white", bg = "black")
		output.config(fg = "white", bg = "black")
	else:
		print("Low Constrast")
		radiusLabel.config(fg = "black", bg = "white")
		heightLabel.config(fg = "black", bg = "white")
		radiusEntry.config(fg = "black", bg = "white")
		heightEntry.config(fg = "black", bg = "white")
		output.config(fg = "black", bg = "white")

#Main Code

file = open("data.txt","w") 
root = tk.Tk()

title = tk.Label(root, text = "Cylinder Volume Calculator")
title.config(fg = "red", bg = "black")
title.pack(fill = tk.BOTH)

radiusLabel = tk.Label(root, text = "Radius: ")
radiusLabel.config(anchor = tk.W)
radiusLabel.pack(fill = tk.BOTH)

radiusEntry = tk.Entry(root)
radiusEntry.config()
radiusEntry.pack(fill = tk.BOTH)

heightLabel = tk.Label(root, text = "Height: ")
heightLabel.config(anchor = tk.W)
heightLabel.pack(fill = tk.BOTH)

heightEntry = tk.Entry(root)
heightEntry.config()
heightEntry.pack(fill = tk.BOTH)

output = tk.Text(root)
output.config(width = 50, height = 10, state = "disabled", borderwidth = 2, relief = "groove")
output.pack()

btnrun = tk.Button(root, text = "Calculate", highlightbackground = "#3E4149")
btnrun.config(fg = "blue", command = runMe)
btnrun.pack(fill = tk.BOTH)

#an integer variable that can be bound to a CheckButton
var = tk.IntVar()
check = tk.Checkbutton(root, text = "High Contrast", variable = var, command = checkSelect)
check.config(anchor = tk.W)
check.pack(fill = tk.BOTH)

root.mainloop()

file.close()

print("END Program")













