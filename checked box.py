from tkinter import *
from tkinter.ttk import *

myroot = Tk()
myroot.geometry('300x200')
myroot.title('Check Button')


def myget():
    if i2.get() == 'check':
        s1.set('Checked')
    else:
        s1.set('Unchecked')


s1 = StringVar()
i2 = StringVar()

myc2 = Checkbutton(myroot, text="check/uncheck", variable=i2, offvalue="uncheck", onvalue='check', command=myget)
myc2.pack()

mye1 = Entry(myroot, font=('Helvetica', 14), textvariable=s1)
mye1.pack()

myroot.mainloop()
