from tkinter import *
from tkinter import Entry

myroot = Tk()
myroot.geometry('300x300')
myroot.resizable(0,0)

myint = DoubleVar()
myint1 = DoubleVar()
myint2 = DoubleVar()

"""myint = IntVar()
myint1 = IntVar()
myint2 = IntVar()"""

MyEntry = Entry(myroot, font = ('Calibri', 12), textvariable = myint)
MyEntry.pack()

MyEntry1 = Entry(myroot, font = ('Calibri', 12), textvariable = myint1)
MyEntry1.pack()

def mydisplay():
    mydata1 = myint.get()
    mydata2 = myint1.get()
    mydata3 = mydata1 - mydata2
    myint2.set(mydata3)

mybtn = Button(myroot, font = ('Calibri',12), text = "difference", command = mydisplay)
mybtn.pack()

MyEntry2 = Entry(myroot, font = ('Calibri', 12), textvariable = myint2)
MyEntry2.pack()
MyEntry2.configure(state = 'readonly')

myroot.mainloop()