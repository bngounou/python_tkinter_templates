from tkinter import *
from tkinter.font import Font

myroot = Tk()
myroot.geometry('300x300')

num1 = BooleanVar()
mystr = StringVar()

def mydatainsertion():
    if num1.get() == True:
        mystr.set('It is set to be true')
    else:
        mystr.set('is set to be false')

"""myc1 = Checkbutton(myroot, variable = num1, text= 'Python',command = mydatainsertion)
myc1.pack()

mye1 = Entry(myroot, width = 20, textvariable = mystr)
mye1.pack()
"""
#==================
"""
myl1 = Label(myroot, text= 'label', anchor = CENTER, font=('Calibri',"18","normal italic overstrike underline"),bd=1,relief='sunken', width=10, height=5)
myl1.pack()
"""
"""
myb1= Button(myroot, text = "withouth highlight thickness")
myb1.grid(row=0, column=1)

myb2= Button(myroot, text = "with highlight thickness", highlightthickness=5)
myb2.grid(row=1, column=1, padx=10, pady=10)
"""
myb1= Button(myroot, text = 'P', font=('Calibri',12), relief=FLAT, bd=4, fg='red', bg='yellow')
myb1.pack(fill=NONE)

myb2= Button(myroot, text = 'Y', font=('Calibri',12), relief=RAISED, bd=4, fg='red', bg='yellow')
myb2.pack(fill=X, padx=10, pady=10)

myb3= Button(myroot, text = 'T', fg='red', bg='LightGreen')
myb3.pack(side=LEFT, fill=Y, padx=10, pady=10)

myb3= Button(myroot, text = 'H', fg='red', bg='Blue')
myb3.pack(side=TOP, fill=X, padx=10, pady=10)

myb4= Button(myroot, text = 'O', bd=4, fg='red', bg='Blue')
myb4.pack(side=BOTTOM, fill=BOTH, padx=10, pady=10)

myb5= Button(myroot, text = 'N', padx=10, pady=10)
myb5.pack(side=RIGHT, fill=BOTH, expand=1, padx=10, pady=10)

"""myb5= Button(myroot, text = 'PYTHON', font=('Calibri',12), relief=RIDGE, cursor= 'star', bd=4)
myb5.pack()
"""

myroot.mainloop()
