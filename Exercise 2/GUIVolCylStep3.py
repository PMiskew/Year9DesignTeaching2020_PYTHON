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
	r = float(r) #cast r to float
	radiusEntry.delete(0, tk.END)

	h = heightEntry.get() #gets value and stores in r
	h = float(h) #casts r to float
	heightEntry.delete(0,tk.END) #deltes content of entry tk.END gets last char

	volume = calcVolumeCylinder(r,h)
	print(volume)

	output.config(state = "normal")
	output.delete("1.0",tk.END) #delete everything

	#string construction
	result = "\n\n\tr\t= "+str(r)+" units\n\th\t= "+str(h)+" units\n\tvolume\t= "+str(volume)+" units\u00B3"
	
	output.insert(tk.END,result)

	output.config(state = "disabled")	





#Main Code
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

check = tk.Checkbutton(root, text = "High Contrast")
check.config(anchor = tk.W)
check.pack(fill = tk.BOTH)

root.mainloop()
print("END Program")













