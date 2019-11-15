import tkinter as tk


root = tk.Tk() #Construct the widget 

f = tk.Frame(root, width = 400, height = 400)
f.grid(row = 0, column = 0, columnspan = 2)

#Inside the frame
textbox1 = tk.Text(f)
textbox1.insert(1.0,"hifajkdsfhasl;kdjhfajkldhfajklsdfhjklasdhfjklasdfhajksdlhfaskljdfhadjklsfhasdjklfhaksdjlfhdakjlshfjkadhjfkl")
textbox1.config(state = "disabled", borderwidth = 2, relief = "groove")

textbox1.pack()

label1 = tk.Label(f, text = "dfjhkaslfhdjklasfhdajsklfhdasklfhasdjklfhadsjklfhadsjklfhadsklfhadjsklfhadsjklfhdaskl")
label1.pack()

root.mainloop()


