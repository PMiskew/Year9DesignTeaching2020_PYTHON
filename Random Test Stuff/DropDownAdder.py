import tkinter as tk


root = tk.Tk()

names = ["Paul","Gavin","Adam","Leo"]

def clicked(*args):
	names.append(entry.get())
	print(oMenuVar.get())
	oMenu.config

def addOption(self, label):
	oMenu.add_command(label=label, command=tk._setit(variable, label, self._command))

entry = tk.Entry(root,)
entry.pack()

button = tk.Button(root, text = "click", command = clicked)
button.pack()

#keeps track of what is actually selected. 
oMenuVar = tk.StringVar();
oMenuVar.set(names[1])
#When you create the menu *names means point to names list 
oMenu = tk.OptionMenu(root,oMenuVar,*names)

oMenu.pack()

MODES = [
        ("Monochrome", "1"),
        ("Grayscale", "L"),
        ("True color", "RGB"),
        ("Color separation", "CMYK"),
    ]

v = tk.StringVar()
v.set("L") # initialize


for text, mode in MODES:
    b = tk.Radiobutton(root, text=text,
                    variable=v, value=mode)
    b.pack(anchor=tk.W)



root.mainloop()