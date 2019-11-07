import tkinter as tk

bgcol = "#021844"
fgcol = "#FFFFFF"
root = tk.Tk()
root.configure(bg = bgcol)

#Construct
titleLabel = tk.Label(root, text = "Auto Information Filler")
#Configure

#Place
titleLabel.grid(row = 0, column = 0, columnspan = 2)
titleLabel.config(bg = bgcol, fg = fgcol, font=("Courier", 24))

entryLabel = tk.Label(root, text = "Enter your name: ")
entryLabel.grid(row = 1, column = 0)

entryName = tk.Entry(root)
entryName.grid(row = 1, column = 1)




root.mainloop()