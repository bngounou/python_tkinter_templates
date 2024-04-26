from tkinter import *

myroot = Tk()
myroot.geometry("300x200")

def myselect():
    mycheck1.select()


def mydeselect():
    mycheck1.deselect()


def mytoggle():
    mycheck1.toggle()


def myinvoke():
    mycheck1.invoke()

mybtn1 = Button(myroot, text='Select', font=('arial', 10), command = myselect)
mybtn1.place(x=50, y=50)
mybtn2 = Button(myroot, text='deSelect', font=('arial', 10), command = mydeselect)
mybtn2.place(x=50, y=100)
mybtn3 = Button(myroot, text='Toggle', font=('arial'), command = mytoggle)
mybtn3.place(x=100, y=50)
mybtn4 = Button(myroot, text='invoque', font=('arial', 8), command = myinvoke)
mybtn4.place(x=100, y=100)
mybtn4.invoke()

mycheck1 = Checkbutton(myroot, text='Check Button')
mycheck1.place(x=50, y=150)
myroot.mainloop()