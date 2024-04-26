from tkinter import *

myroot = Tk()
myroot.geometry('300x300')
myroot.title('CheckButton Widget')

mynum1 = IntVar()
mynum2 = IntVar()
mystr1 = StringVar()

def mydatainsertion():
    if mynum1.get() == 1 and mynum2.get() == 0:
        mystr1.set("Python")

    if mynum1.get() == 0 and mynum2.get() == 1:
        mystr1.set("C#.Net")

    if mynum1.get() == 1 and mynum2.get() == 1:
        mystr1.set("I love both")

    if mynum1.get() == 0 and mynum2.get() == 0:
        mystr1.set("I hate both")


myc1 = Checkbutton(myroot, variable = mynum1, text = "python", command=mydatainsertion)
myc1.pack()

myc2 = Checkbutton(myroot, variable = mynum2, text = "C#.net", command=mydatainsertion)
myc2.pack()

mye1 = Entry(myroot, textvariable = mystr1)
mye1.pack()

myroot.mainloop()