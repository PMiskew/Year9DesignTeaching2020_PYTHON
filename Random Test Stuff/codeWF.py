from tkinter import *
from tkinter import filedialog

#1a2634
#203e5f
#eec550
#f9e3a3
#VARIABLES

#This list stores menu items using the format [day,food]

menuItems = []

days = [
        'Enter Day',
        'Saturday',
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday'
    ]
    
choices = [
    'Choose',
    'Meters',
    'Miles'
]


#FUNCTIONS

def submit():
        print(value)
        cng = str(value)
        print(cng+'lol')

def runMe(*args):
    print("running") 

    main.deiconify() #display main window
    cal.withdraw() #hides cal
    print(cale.get())
    menuItems.append(days1.get())
    menuItems.append(cale.get())
    print(days1.get())
    print(menuItems)

def cal():
   print("test")
   cal.deiconify() #display cal
   main.withdraw() #hides main window

def test():
    print('yeet')


#BUILD MAIN WINDOW
main = Tk()
main.title('Prototype Beta')
main.geometry('500x350')
main.configure(background='#1a2634')

topframe = Frame(main, bg='#eec550',height='30')
topframe.grid(row=0, column=0) # make as wide as main
can1 = Canvas(topframe,height='20',width='125',bg='#eec550',highlightthickness=0)
can1.create_line(0, 5, 20, 5,fill='#203e5f')
can1.create_line(0, 10, 20, 10,fill='#203e5f')
can1.create_line(0, 15, 20, 15,fill='#203e5f')
can1.bind('test',test )
bu1 = Button(topframe, text='Calender', highlightbackground='#eec550', command=cal)
bu2 = Button(topframe, text='Add A Recepie', highlightbackground='#eec550', command=test)
bu3 = Button(topframe, text='Shopping List', highlightbackground='#eec550', command=test)
can1.grid(row=0, column=0)
bu1.grid(row=0, column=1)
bu2.grid(row=0, column=2)
bu3.grid(row=0, column=3, padx=(1, 130))

cal = Frame(main, bg='#203e5f', height='50', width='350')
cal.grid(row=1, column=0)


day1 = Label(cal, text='Monday', bg='#203e5f')
day2 = Label(cal, text='Tuesday', bg='#203e5f')
day3 = Label(cal, text='Wendsday', bg='#203e5f')
day4 = Label(cal, text='Thursday', bg='#203e5f')
day5 = Label(cal, text='Friday', bg='#203e5f')
day6 = Label(cal, text='Saturday', bg='#203e5f')
day7 = Label(cal, text='Sunday', bg='#203e5f')


day1.grid(row=0, column=0)
day2.grid(row=0, column=1)
day3.grid(row=0, column=2)
day4.grid(row=0, column=3)
day5.grid(row=0, column=4)
day6.grid(row=0, column=5)
day7.grid(row=0, column=6)

day1f = Label(cal, text='Food1', bg='#203e5f')
day2f = Label(cal, text='Food2', bg='#203e5f')
day3f = Label(cal, text='Food3', bg='#203e5f')
day4f = Label(cal, text='Food4', bg='#203e5f')
day5f = Label(cal, text='Food5', bg='#203e5f')
day6f = Label(cal, text='Food6', bg='#203e5f')
day7f = Label(cal, text='Food7', bg='#203e5f')

day1f.grid(row=1, column=0)
day2f.grid(row=1, column=1)
day3f.grid(row=1, column=2)
day4f.grid(row=1, column=3)
day5f.grid(row=1, column=4)
day6f.grid(row=1, column=5)
day7f.grid(row=1, column=6)

units1 = StringVar(main)
units2 = StringVar(main)

units1.set('Choose')
units2.set('Choose')

otr = Frame(main, bg='#203e5f', height='50', width='50')
otr.grid(row=2, column=0, pady=(10,0))
conl = Label(otr, text='Easy Converter', bg='#203e5f')
con1 = OptionMenu(otr, units1, *choices)
con2 = OptionMenu(otr, units2, *choices)
conin1 = Entry(otr, highlightbackground='#203e5f')
conin2 = Entry(otr, highlightbackground='#203e5f')
conl.grid(row=0, column=0)
con1.grid(row=1, column=0)
con2.grid(row=1, column=1)
conin1.grid(row=2, column=0)
conin2.grid(row=2, column=1)

pr = Frame(main, bg='#203e5f', height='50', width='50')
pr.grid(row=3, column=0, pady=(10,0))
p1 = Button(pr, text='Print Calender', highlightbackground='#203e5f', command=test)
p2 = Button(pr, text='Print List', highlightbackground='#203e5f', command=test)
p3 = Button(pr, text='Print Recipie', highlightbackground='#203e5f', command=test)
p1.grid(row=0, column=0)
p2.grid(row=1, column=0)
p3.grid(row=2, column=0)

rate = StringVar()

rd = Frame(main, bg='#203e5f', height='50', width='50')
rd.grid(row=4, column=0, pady=(10,0))
la = Label(rd, text='How would you rate your most recent meal?', bg='#203e5f')
r1 = Radiobutton(rd, text='1', variable=rate, value='1', bg='#203e5f')
r2 = Radiobutton(rd, text='2', variable=rate, value='2', bg='#203e5f')
r3 = Radiobutton(rd, text='3', variable=rate, value='3', bg='#203e5f')
r4 = Radiobutton(rd, text='4', variable=rate, value='4', bg='#203e5f')
r5 = Radiobutton(rd, text='5', variable=rate, value='5', bg='#203e5f')
la.grid(row=0, column=0)
r1.grid(row=1, column=1)
r2.grid(row=1, column=2)
r3.grid(row=1, column=3)
r4.grid(row=1, column=4)
r5.grid(row=1, column=5)


#BUILD CALENDAR POPUP**********
cal = Tk()
cal.title('Calender')
cal.configure(background='#1a2634')

days1 = StringVar(cal)
days1.set('Enter Day')

calfr = Frame(cal, bg='#203e5f', height='50', width='50')
calfr.grid(row=0, column=0)

call = Label(calfr, text='Enter Food And Day', bg='#203e5f')
call.grid(row=0, column=0)

cald = OptionMenu(calfr, days1, *days)
cald.grid(row=1, column=0)

cale = Entry(calfr, highlightbackground='#203e5f')
cale.bind("<Return>",runMe)
cale.grid(row=2, column=0)


cal.withdraw() #This hides your window 
main.mainloop()