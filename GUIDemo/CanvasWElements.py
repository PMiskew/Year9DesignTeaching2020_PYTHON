import tkinter as tk

root = tk.Tk()

# create the canvas, size in pixels
canvas = tk.Canvas(width=300, height=200, bg='black')

# pack the canvas into a frame/form
canvas.pack(expand=tk.YES, fill=tk.BOTH)

# load the .gif image file
gif1 = tk.PhotoImage(file='giphy.gif')

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(50, 10, image=gif1, anchor=tk.NW)




root.mainloop()