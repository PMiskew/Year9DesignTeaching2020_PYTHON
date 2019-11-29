import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk



#Varuibles
bgcol = "#021844"
fgcol = "#FFFFFF"


#CORRECTION 1: Lists should be empty 
names = []#this is a list of names
email = []
cc = []
ad = []
cvv = []
city = []
postal = []
expirery = []

#STEP 3 - CREATE DATA FILE
#Need to consider file format
dataFile = open("data.txt","w")

#Functions

def on_closing():
	print("closing")
	#STEP 2 - CREATE MESSAGEBOX
	if messagebox.askokcancel("Quit", "Do you want to quit?"):
		
		for i in range (0, len(names), 1):
			content = names[i]+","+email[i]+","+cc[i]
			dataFile.write(content+"\n")

		root.destroy()

def pushTheButton():
    #messagebox.showinfo("Outcome of pushing the button", " You have pushed the button!")
    #print(entryName.get())
    

    if entryName.get()=="" or entryName2.get() == "" or entryCard.get()=="" or entryAdress.get()=="" or  entryCVV.get() =="" or entryCity.get()=="" or entryPostal.get() =="" or entryExpirery.get() =="":
    	print("One or more of the boxes empty")
    	return #stops function nothing gets saved


    names.append(entryName.get())
    nameListBox = OptionMenu(root, vName, *names)
    nameListBox.grid(row=1, column=2, sticky="W")
    entryName.delete(0,END)
  
    email.append(entryName2.get())
    emailListBox = OptionMenu(root, vAddress, *email)
    emailListBox.grid(row=2, column=2, sticky="W")
    entryName2.delete(0,END)

    cc.append(entryCard.get())
    emailListBox = OptionMenu(root, variable, *cc)
    emailListBox.grid(row=3, column=2, sticky="W")
    entryCard.delete(0,END)

    ad.append(entryAdress.get())
    emailListBox = OptionMenu(root, variable, *ad)
    emailListBox.grid(row=4, column=2, sticky="W")
    entryAdress.delete(0,END)

    cvv.append(entryCVV.get())
    emailListBox = OptionMenu(root, variable, *cvv)
    emailListBox.grid(row=5, column=2, sticky="W")
    entryCVV.delete(0,END)

    city.append(entryCity.get())
    emailListBox = OptionMenu(root, variable, *city)
    emailListBox.grid(row=6, column=2, sticky="W")
    entryCity.delete(0,END)

    postal.append(entryPostal.get())
    emailListBox = OptionMenu(root, variable, *postal)
    emailListBox.grid(row=7, column=2, sticky="W")
    entryPostal.delete(0,END)

    expirery.append(entryExpirery.get())
    emailListBox = OptionMenu(root, variable, *expirery)
    emailListBox.grid(row=8, column=2, sticky="W")
    entryExpirery.delete(0,END)


#def emailPushTheButton():
	#names.append(entryName.get())
	#nameListBox = OptionMenu(root, variable, *names)
	#nameListBox.grid(row=1, column=2, sticky="W")

   



    #print(names)
    #nameListBox.update()





#GUI setup
root = tk.Tk()
root.configure(bg = bgcol)



photoimage = ImageTk.PhotoImage(file="lock-icon.png")


photocanvas = Canvas(root, highlightthickness=0, bg=bgcol, height=60, width=55)

photocanvas.create_image(30, 30, image=photoimage)

photocanvas.grid(row=0, column=2)


variable = IntVar(root)
variable.set("30") # default value

#FontListBox = OptionMenu(root, variable, "saved email")
#FontListBox.config(fg="#243c6a")
#FontListBox.grid(row=1, column=2, sticky="W")



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


entryemail = tk.Label(root, text = "Enter your email: ")
entryemail.grid(row = 2, column = 0)

entryName2 = tk.Entry(root)
entryName2.grid(row = 2, column = 1)

entryCard = tk.Label(root, text = "Credit card number:")
entryCard.grid(row = 3, column = 0)

entryCard = tk.Entry(root)
entryCard.grid(row = 3, column = 1)

entryAdress = tk.Label(root, text = "Enter your addresse:")
entryAdress.grid(row = 4, column = 0)

entryAdress = tk.Entry(root)
entryAdress.grid(row = 4, column = 1)

entryCVV = tk.Label(root, text = "Enter CVV:")
entryCVV.grid(row = 5, column = 0)

entryCVV = tk.Entry(root)
entryCVV.grid(row = 5, column = 1)

entryCity = tk.Label(root, text = "Enter your city:")
entryCity.grid(row = 6, column = 0)

entryCity = tk.Entry(root)
entryCity.grid(row = 6, column = 1)

entryPostal = tk.Label(root, text = "Enter postal code:")
entryPostal.grid(row = 7, column = 0)

entryPostal = tk.Entry(root)
entryPostal.grid(row = 7, column = 1)


entryExpirery = tk.Label(root, text = "Credit card expiery:")
entryExpirery.grid(row = 8, column = 0)

entryExpirery = tk.Entry(root)
entryExpirery.grid(row = 8, column = 1)




variable = StringVar(root)
variable.set("no data") # default value

vName = StringVar(root)
vName.set("no data") # default value

vAddress = StringVar(root)
vAddress.set("no data") # default value


nameListBox = OptionMenu(root, vName,"no data", *names)
nameListBox.config(fg="#243c6a")
nameListBox.grid(row=1, column=2, sticky="W")

emailListBox = OptionMenu(root, vAddress, "no data",*email)
emailListBox.config(fg="#243c6a")
emailListBox .grid(row=2, column=2, sticky="W")

cardListBox = OptionMenu(root, variable, "no data",*cc)
cardListBox.config(fg="#243c6a")
cardListBox.grid(row=3, column=2, sticky="W")

adresseListBox = OptionMenu(root, variable, "no data",*ad)
adresseListBox.config(fg="#243c6a")
adresseListBox.grid(row=4, column=2, sticky="W")

cvvListBox = OptionMenu(root, variable, "no data",*cvv)
cvvListBox.config(fg="#243c6a")
cvvListBox.grid(row=5, column=2, sticky="W")

cityListBox = OptionMenu(root, variable, "no data", *city)
cityListBox.config(fg="#243c6a")
cityListBox.grid(row=6, column=2, sticky="W")

postalListBox = OptionMenu(root, variable, "no data",*postal)
postalListBox.config(fg="#243c6a")
postalListBox.grid(row=7, column=2, sticky="W")

creditListBox = OptionMenu(root, variable, "no data",*expirery)
creditListBox.config(fg="#243c6a")
creditListBox.grid(row=8, column=2, sticky="W")


buttons = []#This creates a list 

#Constructs the buttons
for i in range(0,8,1):
	buttons.append(Button(root, text = "Save", command = pushTheButton))


#Add the buttons
#for i in range(0,8,1):
#	buttons[i].grid(row = 1 + i, column = 3, sticky="W")
button = tk.Button(root, text = "Save", command = pushTheButton)
button.grid(row = 1, column = 3, sticky="W")


#ADD THIS LINE - DEFINE FUNCTION
root.protocol("WM_DELETE_WINDOW", on_closing)



root.mainloop()