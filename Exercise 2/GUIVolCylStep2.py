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

#Main Code
root = tk.Tk()
#Build the widgets and place them in the root before the mainloop
#3 Steps 
#Step 1: Construct the widget
#Step 2: Configure the widget 
#Step 3: place the widget in the root window. "pack it"
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
btnrun.config(fg = "blue")
btnrun.pack(fill = tk.BOTH)

check = tk.Checkbutton(root, text = "High Contrast")
check.config(anchor = tk.W)
check.pack(fill = tk.BOTH)

root.mainloop()
print("END Program")













