import tkinter as tk


root = tk.Tk()

title = tk.Label(root, text = "Word Development Pro")
title.grid(row = 0, column = 0)

canvas = tk.Canvas(root, bg = "black")
canvas.config(width = 30, height = 30)
canvas.grid(row = 0, column = 4)

lab = tk.Label(root, text = "Select Word: ")
lab.grid(row = 1, column = 0)

variable = tk.StringVar(root)
variable.set("one") # default value

wordMenu = tk.OptionMenu(root, variable, "one", "two", "three")
wordMenu.grid(row = 1, column = 1, columnspan = 2)

randomBTN = tk.Button(root, text = "RANDOM")
randomBTN.grid(row = 1, column = 4)

definitionText = tk.Text(root, width = 100, height = 15)
definitionText.grid(row = 2, column = 0, columnspan = 5, padx = 20, pady = 20)

sentenceText = tk.Text(root, width = 100, height = 15)
sentenceText.grid(row = 3, column = 0, columnspan = 5, padx = 20, pady = 20)









root.mainloop()
