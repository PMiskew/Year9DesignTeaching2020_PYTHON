from tkinter import *

root = Tk()

def task():
    print("hello")
    root.after(2000, task)  # reschedule event in 2 seconds

root.after(2000, task)
root.mainloop()