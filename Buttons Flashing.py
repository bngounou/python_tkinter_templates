from tkinter import *

myroot = Tk()

def myselect():
    mycheck2.select()
    mycheck2['selectcolor'] = 'lightgreen'

def mydeselect():
    mycheck2.flash()
    mycheck2['bg'] = 'red'

mycheck1 = Radiobutton(myroot, text="RadioButton1", indicatoron=True, value=2)
mycheck1.place(x=50)
mycheck1.invoke()

mycheck2 = Radiobutton(myroot, text="RadioButton2", indicatoron=False, value=1)
mycheck2.place(x=50,y=50)
mycheck2.invoke()

mybtn1 = Button(myroot, text='select', command=myselect)
mybtn1.place(x=50, y=100)

mybtn2 = Button(myroot, text='deselect', command=mydeselect)
mybtn2.place(x=50, y=150)

myroot.mainloop()