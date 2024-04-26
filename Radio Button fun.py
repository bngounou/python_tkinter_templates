from tkinter import *

myroot = Tk()
myroot.geometry('200x200')

COLOR1 = 'LightBlue'
COLOR2 = 'LightGreen'
COLOR3 = 'Pink'


def mydisplay():
    if myint1.get()==1:
        myroot.configure(background='blue')
    if myint1.get()==2:
        myroot.configure(background='red')
    if myint1.get()==3:
        myroot.configure(background=COLOR3)



myint1 = IntVar()

myrdb1 = Radiobutton(myroot, text=COLOR1, value=1, variable=myint1)
myrdb1.pack()
myrdb2 = Radiobutton(myroot, text=COLOR2, value=2, variable=myint1)
myrdb2.pack()
myrdb3 = Radiobutton(myroot, text=COLOR3, value=3, variable=myint1)
myrdb3.pack()

mybtn1 = Button(myroot, text='Background color', command=mydisplay)
mybtn1.pack()
myroot.mainloop()