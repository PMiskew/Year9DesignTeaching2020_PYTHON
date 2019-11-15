from tkinter import *

root = Tk()

a = Label(root, text="Red", bg="red", fg="white")
a.pack(side=LEFT)
b = Label(root, text="Green", bg="green", fg="black")
b.pack(side=LEFT)
c = Label(root, text="Blue", bg="blue", fg="white")
c.pack(side=LEFT)
d = Label(root, text="Blue", bg="blue", fg="white")
d.pack(side = BOTTOM)


mainloop()