import tkinter as tk


root = tk.Tk()


frame1 = tk.Frame(root, bg = "red", width = 500, height = 100)
frame1.grid(row = 0,column = 0, columnspan = 2);

frame2 = tk.Frame(root, bg = "green", width = 250, height = 400)
frame2.grid(row = 1, column = 0)

frame3 = tk.Frame(root, bg = "yellow", width = 250, height = 400)
frame3.grid(row = 1, column = 1)





root.mainloop()